"""
Views for Tailoring Shop Management System
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum, Count, Q, F
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import date, timedelta
from decimal import Decimal
import json

from .models import (
    Customer, MeasurementProfile, Measurement,
    GarmentType, StitchingType, Order, OrderItem,
    Invoice, Payment, Inventory, Expense
)
from .print_utils import PrintManager
from .forms import (
    CustomerForm, MeasurementProfileForm, MeasurementFormSet,
    OrderForm, OrderItemFormSet, InvoiceForm, PaymentForm,
    InventoryForm, GarmentTypeForm, StitchingTypeForm, QuickBillForm
)


# ============== Authentication ==============

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'shop/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


# ============== Dashboard ==============

@login_required
def dashboard(request):
    today = date.today()
    week_ago = today - timedelta(days=7)
    month_start = today.replace(day=1)
    
    # Today's stats
    today_orders = Order.objects.filter(order_date=today).count()
    today_revenue = Payment.objects.filter(payment_date=today).aggregate(
        total=Sum('amount'))['total'] or Decimal('0.00')
    
    # Orders by status
    pending_orders = Order.objects.filter(status='PENDING').count()
    in_progress_orders = Order.objects.filter(status='IN_PROGRESS').count()
    ready_orders = Order.objects.filter(status='READY').count()
    
    # Overdue orders
    overdue_orders = Order.objects.filter(
        delivery_date__lt=today,
        status__in=['PENDING', 'IN_PROGRESS']
    ).count()
    
    # Monthly revenue
    monthly_revenue = Payment.objects.filter(
        payment_date__gte=month_start
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    
    # Pending payments
    pending_payments = Invoice.objects.annotate(
        paid=Sum('payments__amount')
    ).filter(
        Q(paid__lt=F('total')) | Q(paid__isnull=True)
    ).count()
    
    # Recent orders
    recent_orders = Order.objects.select_related('customer').order_by('-created_at')[:10]
    
    # Today's deliveries
    today_deliveries = Order.objects.filter(
        delivery_date=today,
        status__in=['PENDING', 'IN_PROGRESS', 'READY']
    ).select_related('customer')
    
    # Low stock items
    low_stock_items = Inventory.objects.filter(
        quantity__lte=F('min_stock_level')
    )[:5]
    
    context = {
        'today_orders': today_orders,
        'today_revenue': today_revenue,
        'pending_orders': pending_orders,
        'in_progress_orders': in_progress_orders,
        'ready_orders': ready_orders,
        'overdue_orders': overdue_orders,
        'monthly_revenue': monthly_revenue,
        'pending_payments': pending_payments,
        'recent_orders': recent_orders,
        'today_deliveries': today_deliveries,
        'low_stock_items': low_stock_items,
    }
    return render(request, 'shop/dashboard.html', context)


# ============== Customer Management ==============

@login_required
def customer_list(request):
    query = request.GET.get('q', '')
    customers = Customer.objects.all()
    
    if query:
        customers = customers.filter(
            Q(name__icontains=query) | 
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    
    paginator = Paginator(customers, 20)
    page = request.GET.get('page')
    customers = paginator.get_page(page)
    
    return render(request, 'shop/customer_list.html', {'customers': customers, 'query': query})


@login_required
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Customer "{customer.name}" added successfully!')
            
            # Check if coming from quick billing
            if request.GET.get('next') == 'billing':
                return redirect('quick_billing')
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    
    return render(request, 'shop/customer_form.html', {'form': form, 'title': 'Add Customer'})


@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    orders = customer.orders.all()[:10]
    profiles = customer.measurement_profiles.filter(is_active=True)
    
    # Calculate stats
    total_orders = customer.orders.count()
    total_spent = Invoice.objects.filter(
        order__customer=customer
    ).aggregate(total=Sum('total'))['total'] or Decimal('0.00')
    
    context = {
        'customer': customer,
        'orders': orders,
        'profiles': profiles,
        'total_orders': total_orders,
        'total_spent': total_spent,
    }
    return render(request, 'shop/customer_detail.html', context)


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully!')
            return redirect('customer_detail', pk=pk)
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'shop/customer_form.html', {'form': form, 'title': 'Edit Customer', 'customer': customer})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        name = customer.name
        customer.delete()
        messages.success(request, f'Customer "{name}" deleted.')
        return redirect('customer_list')
    return render(request, 'shop/customer_confirm_delete.html', {'customer': customer})


@login_required
def customer_search(request):
    """AJAX search for customers"""
    query = request.GET.get('q', '')
    customers = Customer.objects.filter(
        Q(name__icontains=query) | Q(phone__icontains=query)
    )[:10]
    
    data = [{
        'id': c.id,
        'name': c.name,
        'phone': c.phone,
        'address': c.address or '',
    } for c in customers]
    
    return JsonResponse({'customers': data})


# ============== Measurements ==============

@login_required
def measurement_list(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    profiles = customer.measurement_profiles.filter(is_active=True)
    return render(request, 'shop/measurement_list.html', {'customer': customer, 'profiles': profiles})


@login_required
def measurement_add(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    
    if request.method == 'POST':
        profile_form = MeasurementProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.customer = customer
            profile.save()
            
            # Process measurements from POST data
            measurements_data = request.POST.getlist('measurement_key')
            values = request.POST.getlist('measurement_value')
            units = request.POST.getlist('measurement_unit')
            
            for i, key in enumerate(measurements_data):
                if key and values[i]:
                    Measurement.objects.create(
                        profile=profile,
                        measurement_key=key,
                        measurement_value=Decimal(values[i]),
                        unit=units[i] if i < len(units) else 'inch'
                    )
            
            messages.success(request, 'Measurements saved successfully!')
            return redirect('customer_detail', pk=customer_id)
    else:
        profile_form = MeasurementProfileForm()
    
    measurement_keys = Measurement.MEASUREMENT_KEYS
    return render(request, 'shop/measurement_form.html', {
        'customer': customer,
        'profile_form': profile_form,
        'measurement_keys': measurement_keys,
        'title': 'Add Measurements'
    })


@login_required
def measurement_edit(request, profile_id):
    profile = get_object_or_404(MeasurementProfile, pk=profile_id)
    customer = profile.customer
    
    if request.method == 'POST':
        profile_form = MeasurementProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            
            # Clear existing and re-add
            profile.measurements.all().delete()
            
            measurements_data = request.POST.getlist('measurement_key')
            values = request.POST.getlist('measurement_value')
            units = request.POST.getlist('measurement_unit')
            
            for i, key in enumerate(measurements_data):
                if key and values[i]:
                    Measurement.objects.create(
                        profile=profile,
                        measurement_key=key,
                        measurement_value=Decimal(values[i]),
                        unit=units[i] if i < len(units) else 'inch'
                    )
            
            messages.success(request, 'Measurements updated!')
            return redirect('customer_detail', pk=customer.pk)
    else:
        profile_form = MeasurementProfileForm(instance=profile)
    
    existing_measurements = {m.measurement_key: m for m in profile.measurements.all()}
    measurement_keys = Measurement.MEASUREMENT_KEYS
    
    return render(request, 'shop/measurement_form.html', {
        'customer': customer,
        'profile': profile,
        'profile_form': profile_form,
        'measurement_keys': measurement_keys,
        'existing_measurements': existing_measurements,
        'title': 'Edit Measurements'
    })


# ============== Orders ==============

@login_required
def order_list(request):
    status = request.GET.get('status', '')
    query = request.GET.get('q', '')
    
    orders = Order.objects.select_related('customer').prefetch_related('items')
    
    if status:
        orders = orders.filter(status=status)
    if query:
        orders = orders.filter(
            Q(order_number__icontains=query) |
            Q(customer__name__icontains=query) |
            Q(customer__phone__icontains=query)
        )
    
    paginator = Paginator(orders, 20)
    page = request.GET.get('page')
    orders = paginator.get_page(page)
    
    status_choices = Order.STATUS_CHOICES
    return render(request, 'shop/order_list.html', {
        'orders': orders,
        'status': status,
        'query': query,
        'status_choices': status_choices
    })


@login_required
def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user
            order.save()
            
            # Process order items
            garment_types = request.POST.getlist('garment_type')
            stitching_types = request.POST.getlist('stitching_type')
            quantities = request.POST.getlist('quantity')
            prices = request.POST.getlist('price')
            item_notes = request.POST.getlist('item_notes')
            
            for i in range(len(garment_types)):
                if garment_types[i] and prices[i]:
                    OrderItem.objects.create(
                        order=order,
                        garment_type_id=garment_types[i],
                        stitching_type_id=stitching_types[i],
                        quantity=int(quantities[i]) if quantities[i] else 1,
                        price=Decimal(prices[i]),
                        notes=item_notes[i] if i < len(item_notes) else ''
                    )
            
            messages.success(request, f'Order {order.order_number} created!')
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    
    garment_types = GarmentType.objects.filter(is_active=True)
    stitching_types = StitchingType.objects.filter(is_active=True)
    
    return render(request, 'shop/order_form.html', {
        'form': form,
        'garment_types': garment_types,
        'stitching_types': stitching_types,
        'title': 'New Order'
    })


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order.objects.select_related('customer', 'invoice'), pk=pk)
    items = order.items.select_related('garment_type', 'stitching_type')
    
    has_invoice = hasattr(order, 'invoice')
    invoice = order.invoice if has_invoice else None
    
    return render(request, 'shop/order_detail.html', {
        'order': order,
        'items': items,
        'invoice': invoice,
        'has_invoice': has_invoice
    })


@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
            # Update items
            order.items.all().delete()
            
            garment_types = request.POST.getlist('garment_type')
            stitching_types = request.POST.getlist('stitching_type')
            quantities = request.POST.getlist('quantity')
            prices = request.POST.getlist('price')
            item_notes = request.POST.getlist('item_notes')
            
            for i in range(len(garment_types)):
                if garment_types[i] and prices[i]:
                    OrderItem.objects.create(
                        order=order,
                        garment_type_id=garment_types[i],
                        stitching_type_id=stitching_types[i],
                        quantity=int(quantities[i]) if quantities[i] else 1,
                        price=Decimal(prices[i]),
                        notes=item_notes[i] if i < len(item_notes) else ''
                    )
            
            messages.success(request, 'Order updated!')
            return redirect('order_detail', pk=pk)
    else:
        form = OrderForm(instance=order)
    
    garment_types = GarmentType.objects.filter(is_active=True)
    stitching_types = StitchingType.objects.filter(is_active=True)
    items = order.items.all()
    
    return render(request, 'shop/order_form.html', {
        'form': form,
        'order': order,
        'items': items,
        'garment_types': garment_types,
        'stitching_types': stitching_types,
        'title': 'Edit Order'
    })


@login_required
def order_status_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Order status updated to {order.get_status_display()}')
    return redirect('order_detail', pk=pk)


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order_number = order.order_number
        order.delete()
        messages.success(request, f'Order {order_number} deleted.')
        return redirect('order_list')
    return render(request, 'shop/order_confirm_delete.html', {'order': order})


# ============== Quick Billing ==============

@login_required
def quick_billing(request):
    """Main quick billing interface"""
    customers = Customer.objects.all()[:50]
    garment_types = GarmentType.objects.filter(is_active=True)
    stitching_types = StitchingType.objects.filter(is_active=True)
    
    return render(request, 'shop/quick_billing.html', {
        'customers': customers,
        'garment_types': garment_types,
        'stitching_types': stitching_types,
    })


@login_required
def create_bill(request):
    """Process quick bill creation"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get or create customer
            customer_id = data.get('customer_id')
            if customer_id:
                customer = Customer.objects.get(pk=customer_id)
            else:
                # Create new customer
                customer = Customer.objects.create(
                    name=data.get('customer_name'),
                    phone=data.get('customer_phone'),
                    address=data.get('customer_address', '')
                )
            
            # Create order
            order = Order.objects.create(
                customer=customer,
                delivery_date=data.get('delivery_date') or None,
                priority=data.get('priority', 'NORMAL'),
                notes=data.get('notes', ''),
                created_by=request.user
            )
            
            # Create order items
            items = data.get('items', [])
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    garment_type_id=item['garment_type'],
                    stitching_type_id=item['stitching_type'],
                    quantity=int(item.get('quantity', 1)),
                    price=Decimal(str(item['price'])),
                    notes=item.get('notes', '')
                )
            
            # Create invoice
            subtotal = Decimal(str(data.get('subtotal', 0)))
            discount = Decimal(str(data.get('discount', 0)))
            tax = Decimal(str(data.get('tax', 0)))
            total = Decimal(str(data.get('total', 0)))
            
            invoice = Invoice.objects.create(
                order=order,
                subtotal=subtotal,
                discount=discount,
                tax=tax,
                total=total
            )
            
            # Record advance payment if any
            advance = Decimal(str(data.get('advance', 0)))
            if advance > 0:
                Payment.objects.create(
                    invoice=invoice,
                    amount=advance,
                    payment_mode=data.get('payment_mode', 'CASH'),
                    received_by=request.user
                )
            
            return JsonResponse({
                'success': True,
                'order_id': order.pk,
                'order_number': order.order_number,
                'invoice_id': invoice.pk,
                'invoice_number': invoice.invoice_number
            })
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


# ============== Invoices ==============

@login_required
def invoice_list(request):
    status = request.GET.get('status', '')
    query = request.GET.get('q', '')
    
    invoices = Invoice.objects.select_related('order', 'order__customer').prefetch_related('payments')
    
    if query:
        invoices = invoices.filter(
            Q(invoice_number__icontains=query) |
            Q(order__order_number__icontains=query) |
            Q(order__customer__name__icontains=query)
        )
    
    # Filter by payment status
    if status == 'paid':
        invoices = [i for i in invoices if i.is_fully_paid]
    elif status == 'partial':
        invoices = [i for i in invoices if i.paid_amount > 0 and not i.is_fully_paid]
    elif status == 'unpaid':
        invoices = [i for i in invoices if i.paid_amount == 0]
    
    return render(request, 'shop/invoice_list.html', {
        'invoices': invoices,
        'status': status,
        'query': query
    })


@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice.objects.select_related('order', 'order__customer'), pk=pk)
    payments = invoice.payments.all()
    items = invoice.order.items.select_related('garment_type', 'stitching_type')
    
    return render(request, 'shop/invoice_detail.html', {
        'invoice': invoice,
        'payments': payments,
        'items': items
    })


@login_required
def invoice_print(request, pk):
    invoice = get_object_or_404(Invoice.objects.select_related('order', 'order__customer'), pk=pk)
    items = invoice.order.items.select_related('garment_type', 'stitching_type')
    payments = invoice.payments.all()
    
    return render(request, 'shop/invoice_print.html', {
        'invoice': invoice,
        'items': items,
        'payments': payments
    })


@login_required
def invoice_create(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if hasattr(order, 'invoice'):
        messages.warning(request, 'Invoice already exists for this order.')
        return redirect('invoice_detail', pk=order.invoice.pk)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.order = order
            invoice.save()
            messages.success(request, f'Invoice {invoice.invoice_number} created!')
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        subtotal = order.total_amount
        form = InvoiceForm(initial={
            'subtotal': subtotal,
            'total': subtotal
        })
    
    return render(request, 'shop/invoice_form.html', {
        'form': form,
        'order': order,
        'title': 'Create Invoice'
    })


# ============== Payments ==============

@login_required
def payment_add(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.invoice = invoice
            payment.received_by = request.user
            payment.save()
            messages.success(request, f'Payment of ₹{payment.amount} recorded!')
            return redirect('invoice_detail', pk=invoice_id)
    else:
        form = PaymentForm(initial={'amount': invoice.balance_amount})
    
    return render(request, 'shop/payment_form.html', {
        'form': form,
        'invoice': invoice
    })


@login_required
def payment_list(request):
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    mode = request.GET.get('mode', '')
    
    payments = Payment.objects.select_related('invoice', 'invoice__order', 'invoice__order__customer')
    
    if start_date:
        payments = payments.filter(payment_date__gte=start_date)
    if end_date:
        payments = payments.filter(payment_date__lte=end_date)
    if mode:
        payments = payments.filter(payment_mode=mode)
    
    total = payments.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    
    paginator = Paginator(payments, 50)
    page = request.GET.get('page')
    payments = paginator.get_page(page)
    
    return render(request, 'shop/payment_list.html', {
        'payments': payments,
        'total': total,
        'start_date': start_date,
        'end_date': end_date,
        'mode': mode,
        'payment_modes': Payment.PAYMENT_MODE_CHOICES
    })


# ============== Inventory ==============

@login_required
def inventory_list(request):
    query = request.GET.get('q', '')
    show_low_stock = request.GET.get('low_stock', '')
    
    items = Inventory.objects.all()
    
    if query:
        items = items.filter(item_name__icontains=query)
    if show_low_stock:
        items = items.filter(quantity__lte=F('min_stock_level'))
    
    return render(request, 'shop/inventory_list.html', {
        'items': items,
        'query': query,
        'show_low_stock': show_low_stock
    })


@login_required
def inventory_add(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory item added!')
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    
    return render(request, 'shop/inventory_form.html', {'form': form, 'title': 'Add Inventory Item'})


@login_required
def inventory_edit(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory item updated!')
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=item)
    
    return render(request, 'shop/inventory_form.html', {'form': form, 'item': item, 'title': 'Edit Inventory Item'})


@login_required
def inventory_delete(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Inventory item deleted.')
        return redirect('inventory_list')
    return render(request, 'shop/inventory_confirm_delete.html', {'item': item})


# ============== Settings ==============

@login_required
def settings_view(request):
    garment_types = GarmentType.objects.all()
    stitching_types = StitchingType.objects.all()
    
    return render(request, 'shop/settings.html', {
        'garment_types': garment_types,
        'stitching_types': stitching_types
    })


@login_required
def garment_types(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            form = GarmentTypeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Garment type added!')
        elif action == 'edit':
            pk = request.POST.get('pk')
            item = get_object_or_404(GarmentType, pk=pk)
            form = GarmentTypeForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, 'Garment type updated!')
        elif action == 'delete':
            pk = request.POST.get('pk')
            item = get_object_or_404(GarmentType, pk=pk)
            item.delete()
            messages.success(request, 'Garment type deleted!')
        
        return redirect('garment_types')
    
    items = GarmentType.objects.all()
    form = GarmentTypeForm()
    
    return render(request, 'shop/garment_types.html', {'items': items, 'form': form})


@login_required
def stitching_types(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            form = StitchingTypeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Stitching type added!')
        elif action == 'edit':
            pk = request.POST.get('pk')
            item = get_object_or_404(StitchingType, pk=pk)
            form = StitchingTypeForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, 'Stitching type updated!')
        elif action == 'delete':
            pk = request.POST.get('pk')
            item = get_object_or_404(StitchingType, pk=pk)
            item.delete()
            messages.success(request, 'Stitching type deleted!')
        
        return redirect('stitching_types')
    
    items = StitchingType.objects.all()
    form = StitchingTypeForm()
    
    return render(request, 'shop/stitching_types.html', {'items': items, 'form': form})


# ============== Reports ==============

@login_required
def reports(request):
    return render(request, 'shop/reports.html')


@login_required
def sales_report(request):
    start_date = request.GET.get('start_date', str(date.today().replace(day=1)))
    end_date = request.GET.get('end_date', str(date.today()))
    
    invoices = Invoice.objects.filter(
        created_at__date__gte=start_date,
        created_at__date__lte=end_date
    ).select_related('order', 'order__customer')
    
    total_sales = invoices.aggregate(total=Sum('total'))['total'] or Decimal('0.00')
    total_received = Payment.objects.filter(
        payment_date__gte=start_date,
        payment_date__lte=end_date
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    
    # By payment mode
    by_mode = Payment.objects.filter(
        payment_date__gte=start_date,
        payment_date__lte=end_date
    ).values('payment_mode').annotate(total=Sum('amount'))
    
    return render(request, 'shop/sales_report.html', {
        'invoices': invoices,
        'total_sales': total_sales,
        'total_received': total_received,
        'by_mode': by_mode,
        'start_date': start_date,
        'end_date': end_date
    })


@login_required
def customer_report(request):
    customers = Customer.objects.annotate(
        order_count=Count('orders'),
        total_spent=Sum('orders__invoice__total')
    ).order_by('-total_spent')[:50]
    
    return render(request, 'shop/customer_report.html', {'customers': customers})


# ============== API Endpoints ==============

@login_required
def api_customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    profiles = customer.measurement_profiles.filter(is_active=True)
    
    data = {
        'id': customer.id,
        'name': customer.name,
        'phone': customer.phone,
        'address': customer.address or '',
        'profiles': [{
            'id': p.id,
            'name': p.profile_name,
            'measurements': [{
                'key': m.get_measurement_key_display(),
                'value': str(m.measurement_value),
                'unit': m.unit
            } for m in p.measurements.all()]
        } for p in profiles]
    }
    
    return JsonResponse(data)


@login_required
def api_calculate_price(request):
    garment_id = request.GET.get('garment_id')
    stitching_id = request.GET.get('stitching_id')
    
    try:
        garment = GarmentType.objects.get(pk=garment_id)
        stitching = StitchingType.objects.get(pk=stitching_id)
        
        price = (garment.base_price * stitching.price_multiplier) + stitching.extra_charge
        
        return JsonResponse({
            'success': True,
            'price': str(price),
            'garment_price': str(garment.base_price),
            'multiplier': str(stitching.price_multiplier),
            'extra': str(stitching.extra_charge)
        })
    except (GarmentType.DoesNotExist, StitchingType.DoesNotExist):
        return JsonResponse({'success': False, 'error': 'Invalid selection'}, status=400)


@login_required
def api_dashboard_stats(request):
    today = date.today()
    
    data = {
        'today_orders': Order.objects.filter(order_date=today).count(),
        'pending_orders': Order.objects.filter(status='PENDING').count(),
        'ready_orders': Order.objects.filter(status='READY').count(),
        'today_revenue': str(Payment.objects.filter(payment_date=today).aggregate(
            total=Sum('amount'))['total'] or '0.00')
    }
    
    return JsonResponse(data)


# Print Views
@login_required
def print_invoice(request, invoice_id):
    """Generate and download invoice PDF"""
    try:
        invoice = get_object_or_404(Invoice, id=invoice_id)
        pdf_content = PrintManager.generate_invoice_pdf(invoice)
        
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Invoice_{invoice.invoice_number}.pdf"'
        return response
    except Exception as e:
        messages.error(request, f"Error generating invoice PDF: {str(e)}")
        return redirect('invoice_list')


@login_required
def print_receipt(request, payment_id):
    """Generate and download receipt PDF"""
    try:
        payment = get_object_or_404(Payment, id=payment_id)
        pdf_content = PrintManager.generate_receipt_pdf(payment)
        
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Receipt_{payment_id}.pdf"'
        return response
    except Exception as e:
        messages.error(request, f"Error generating receipt PDF: {str(e)}")
        return redirect('payment_list')


@login_required
def invoice_preview(request, invoice_id):
    """Preview invoice before printing"""
    invoice = get_object_or_404(Invoice, id=invoice_id)
    try:
        pdf_content = PrintManager.generate_invoice_pdf(invoice)
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Invoice_{invoice.invoice_number}.pdf"'
        return response
    except Exception as e:
        messages.error(request, f"Error previewing invoice: {str(e)}")
        return redirect('invoice_detail', pk=invoice_id)


@login_required
def receipt_preview(request, payment_id):
    """Preview receipt before printing"""
    payment = get_object_or_404(Payment, id=payment_id)
    try:
        pdf_content = PrintManager.generate_receipt_pdf(payment)
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Receipt_{payment_id}.pdf"'
        return response
    except Exception as e:
        messages.error(request, f"Error previewing receipt: {str(e)}")
        return redirect('payment_detail', pk=payment_id)
