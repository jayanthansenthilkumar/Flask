"""
Models for Tailoring Shop Management System
Based on the provided database schema with enhancements
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
import uuid
from datetime import date


class ShopUser(models.Model):
    """Extended user profile for shop staff"""
    ROLE_CHOICES = [
        ('OWNER', 'Owner'),
        ('STAFF', 'Staff'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop_profile')
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STAFF')
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"

    class Meta:
        verbose_name = 'Shop User'
        verbose_name_plural = 'Shop Users'


class Customer(models.Model):
    """Customer information"""
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"

    @property
    def total_orders(self):
        return self.orders.count()

    @property
    def pending_amount(self):
        total = Decimal('0.00')
        for order in self.orders.all():
            if hasattr(order, 'invoice'):
                paid = order.invoice.payments.aggregate(
                    total=models.Sum('amount')
                )['total'] or Decimal('0.00')
                total += order.invoice.total - paid
        return total

    class Meta:
        ordering = ['-created_at']


class MeasurementProfile(models.Model):
    """Measurement profiles for customers (can have multiple)"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='measurement_profiles')
    profile_name = models.CharField(max_length=50, default='Default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} - {self.profile_name}"

    class Meta:
        unique_together = ['customer', 'profile_name']


class Measurement(models.Model):
    """Individual measurements (atomic key-value pairs)"""
    UNIT_CHOICES = [
        ('cm', 'Centimeters'),
        ('inch', 'Inches'),
    ]
    
    # Common measurement keys
    MEASUREMENT_KEYS = [
        ('chest', 'Chest'),
        ('waist', 'Waist'),
        ('hip', 'Hip'),
        ('shoulder', 'Shoulder'),
        ('sleeve_length', 'Sleeve Length'),
        ('arm_hole', 'Arm Hole'),
        ('neck', 'Neck'),
        ('shirt_length', 'Shirt Length'),
        ('pant_length', 'Pant Length'),
        ('inseam', 'Inseam'),
        ('thigh', 'Thigh'),
        ('knee', 'Knee'),
        ('bottom', 'Bottom'),
        ('cuff', 'Cuff'),
        ('back_length', 'Back Length'),
        ('front_length', 'Front Length'),
        ('blouse_length', 'Blouse Length'),
        ('bust', 'Bust'),
        ('underbust', 'Under Bust'),
        ('custom', 'Custom'),
    ]
    
    profile = models.ForeignKey(MeasurementProfile, on_delete=models.CASCADE, related_name='measurements')
    measurement_key = models.CharField(max_length=50, choices=MEASUREMENT_KEYS)
    custom_key = models.CharField(max_length=50, blank=True, null=True)
    measurement_value = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='inch')

    def __str__(self):
        key = self.custom_key if self.measurement_key == 'custom' else self.get_measurement_key_display()
        return f"{key}: {self.measurement_value} {self.unit}"

    class Meta:
        ordering = ['measurement_key']


class GarmentType(models.Model):
    """Pre-defined garment types with default pricing"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class StitchingType(models.Model):
    """Stitching types with price multipliers"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)
    extra_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Order(models.Model):
    """Main order record"""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('READY', 'Ready for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    PRIORITY_CHOICES = [
        ('NORMAL', 'Normal'),
        ('URGENT', 'Urgent'),
        ('EXPRESS', 'Express'),
    ]

    order_number = models.CharField(max_length=20, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    profile = models.ForeignKey(MeasurementProfile, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField(default=date.today)
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='NORMAL')
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate unique order number: ORD-YYYYMMDD-XXXX
            today = date.today()
            prefix = f"ORD-{today.strftime('%Y%m%d')}"
            last_order = Order.objects.filter(order_number__startswith=prefix).order_by('-order_number').first()
            if last_order:
                last_num = int(last_order.order_number.split('-')[-1])
                new_num = last_num + 1
            else:
                new_num = 1
            self.order_number = f"{prefix}-{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_number} - {self.customer.name}"

    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def is_overdue(self):
        if self.delivery_date and self.status not in ['DELIVERED', 'CANCELLED']:
            return date.today() > self.delivery_date
        return False

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    """Individual items in an order"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    garment_type = models.ForeignKey(GarmentType, on_delete=models.PROTECT)
    stitching_type = models.ForeignKey(StitchingType, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    notes = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.garment_type.name} x {self.quantity}"

    @property
    def total_price(self):
        return self.price * self.quantity

    def calculate_price(self):
        """Auto-calculate price based on garment and stitching type"""
        base = self.garment_type.base_price
        multiplier = self.stitching_type.price_multiplier
        extra = self.stitching_type.extra_charge
        return (base * multiplier) + extra


class Invoice(models.Model):
    """Invoice for orders"""
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='invoice')
    invoice_number = models.CharField(max_length=30, unique=True, editable=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_type = models.CharField(max_length=10, choices=[('FLAT', 'Flat'), ('PERCENT', 'Percentage')], default='FLAT')
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            # Generate unique invoice number: INV-YYYYMMDD-XXXX
            today = date.today()
            prefix = f"INV-{today.strftime('%Y%m%d')}"
            last_invoice = Invoice.objects.filter(invoice_number__startswith=prefix).order_by('-invoice_number').first()
            if last_invoice:
                last_num = int(last_invoice.invoice_number.split('-')[-1])
                new_num = last_num + 1
            else:
                new_num = 1
            self.invoice_number = f"{prefix}-{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.invoice_number} - ₹{self.total}"

    @property
    def paid_amount(self):
        return self.payments.aggregate(total=models.Sum('amount'))['total'] or Decimal('0.00')

    @property
    def balance_amount(self):
        return self.total - self.paid_amount

    @property
    def is_fully_paid(self):
        return self.balance_amount <= 0

    @property
    def payment_status(self):
        if self.is_fully_paid:
            return 'PAID'
        elif self.paid_amount > 0:
            return 'PARTIAL'
        return 'UNPAID'

    class Meta:
        ordering = ['-created_at']


class Payment(models.Model):
    """Payment records (supports partial payments)"""
    PAYMENT_MODE_CHOICES = [
        ('CASH', 'Cash'),
        ('UPI', 'UPI'),
        ('CARD', 'Card'),
        ('BANK', 'Bank Transfer'),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField(default=date.today)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, default='CASH')
    reference_number = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"₹{self.amount} - {self.payment_mode} ({self.payment_date})"

    class Meta:
        ordering = ['-payment_date', '-created_at']


class Inventory(models.Model):
    """Inventory management for materials"""
    UNIT_CHOICES = [
        ('meters', 'Meters'),
        ('yards', 'Yards'),
        ('pieces', 'Pieces'),
        ('rolls', 'Rolls'),
        ('boxes', 'Boxes'),
        ('kg', 'Kilograms'),
    ]

    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='meters')
    min_stock_level = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    supplier = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.quantity} {self.unit}"

    @property
    def is_low_stock(self):
        return self.quantity <= self.min_stock_level

    class Meta:
        verbose_name_plural = 'Inventory'
        ordering = ['item_name']


class ExpenseCategory(models.Model):
    """Categories for expenses"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Expense Categories'


class Expense(models.Model):
    """Track shop expenses"""
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField(default=date.today)
    payment_mode = models.CharField(max_length=20, choices=Payment.PAYMENT_MODE_CHOICES, default='CASH')
    reference = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} - ₹{self.amount}"

    class Meta:
        ordering = ['-expense_date', '-created_at']
