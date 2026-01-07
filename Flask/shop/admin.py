from django.contrib import admin
from .models import (
    ShopUser, Customer, MeasurementProfile, Measurement,
    GarmentType, StitchingType, Order, OrderItem,
    Invoice, Payment, Inventory, ExpenseCategory, Expense
)


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'phone', 'is_active', 'created_at']
    list_filter = ['role', 'is_active']
    search_fields = ['full_name', 'phone']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    search_fields = ['name', 'phone', 'email']


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1


@admin.register(MeasurementProfile)
class MeasurementProfileAdmin(admin.ModelAdmin):
    list_display = ['customer', 'profile_name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['customer__name', 'profile_name']
    inlines = [MeasurementInline]


@admin.register(GarmentType)
class GarmentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'is_active']
    list_filter = ['is_active']


@admin.register(StitchingType)
class StitchingTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_multiplier', 'extra_charge', 'is_active']
    list_filter = ['is_active']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer', 'status', 'priority', 'order_date', 'delivery_date']
    list_filter = ['status', 'priority']
    search_fields = ['order_number', 'customer__name', 'customer__phone']
    inlines = [OrderItemInline]


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'order', 'total', 'paid_amount', 'balance_amount', 'created_at']
    search_fields = ['invoice_number', 'order__order_number']
    inlines = [PaymentInline]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity', 'unit', 'min_stock_level', 'is_low_stock']
    list_filter = ['unit']
    search_fields = ['item_name']


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'description', 'amount', 'expense_date', 'payment_mode']
    list_filter = ['category', 'payment_mode', 'expense_date']
    search_fields = ['description']
