"""
Forms for Tailoring Shop Management System
"""
from django import forms
from django.forms import inlineformset_factory
from .models import (
    Customer, MeasurementProfile, Measurement,
    GarmentType, StitchingType, Order, OrderItem,
    Invoice, Payment, Inventory
)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (optional)'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Notes'}),
        }


class MeasurementProfileForm(forms.ModelForm):
    class Meta:
        model = MeasurementProfile
        fields = ['profile_name']
        widgets = {
            'profile_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profile Name (e.g., Default, Formal, Casual)'}),
        }


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['measurement_key', 'measurement_value', 'unit']
        widgets = {
            'measurement_key': forms.Select(attrs={'class': 'form-select'}),
            'measurement_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.25'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
        }


MeasurementFormSet = inlineformset_factory(
    MeasurementProfile, Measurement,
    form=MeasurementForm,
    extra=10, can_delete=True
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'profile', 'delivery_date', 'priority', 'notes']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select', 'id': 'customer-select'}),
            'profile': forms.Select(attrs={'class': 'form-select'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()
        self.fields['profile'].required = False


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['garment_type', 'stitching_type', 'quantity', 'price', 'notes']
        widgets = {
            'garment_type': forms.Select(attrs={'class': 'form-select garment-select'}),
            'stitching_type': forms.Select(attrs={'class': 'form-select stitching-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control quantity-input', 'value': 1, 'min': 1}),
            'price': forms.NumberInput(attrs={'class': 'form-control price-input', 'step': '0.01'}),
            'notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item notes'}),
        }


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem,
    form=OrderItemForm,
    extra=3, can_delete=True
)


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['subtotal', 'discount', 'discount_type', 'tax_rate', 'tax', 'total', 'notes']
        widgets = {
            'subtotal': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'discount_type': forms.Select(attrs={'class': 'form-select'}),
            'tax_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_mode', 'payment_date', 'reference_number', 'notes']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'payment_mode': forms.Select(attrs={'class': 'form-select'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference/Transaction ID'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'description', 'quantity', 'unit', 'min_stock_level', 'cost_per_unit', 'supplier']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'min_stock_level': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cost_per_unit': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GarmentTypeForm(forms.ModelForm):
    class Meta:
        model = GarmentType
        fields = ['name', 'description', 'base_price', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'base_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class StitchingTypeForm(forms.ModelForm):
    class Meta:
        model = StitchingType
        fields = ['name', 'description', 'price_multiplier', 'extra_charge', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'price_multiplier': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'extra_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class QuickBillForm(forms.Form):
    """Form for quick billing interface"""
    customer_name = forms.CharField(max_length=100, required=False)
    customer_phone = forms.CharField(max_length=15, required=False)
    customer_id = forms.IntegerField(required=False)
    delivery_date = forms.DateField(required=False)
    priority = forms.ChoiceField(choices=Order.PRIORITY_CHOICES, initial='NORMAL')
    discount = forms.DecimalField(max_digits=10, decimal_places=2, initial=0)
    advance = forms.DecimalField(max_digits=10, decimal_places=2, initial=0)
    payment_mode = forms.ChoiceField(choices=Payment.PAYMENT_MODE_CHOICES, initial='CASH')
