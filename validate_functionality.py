"""
Functionality Validation Script for SriJai Tailoring Management System
This script validates all backend functionalities, routes, and database operations.
"""
import os
import django
from django.test import TestCase
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test.client import Client
from django.contrib.auth import get_user_model
from django.urls import reverse
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tailor_shop.settings')
django.setup()

from shop.models import *

def validate_all_functionalities():
    """Validate all system functionalities."""
    print("\n" + "="*60)
    print("SriJai Tailoring - Functionality Validation")
    print("="*60 + "\n")
    
    client = Client()
    User = get_user_model()
    
    # 1. Database Models Validation
    print("1. 📊 Database Models Validation")
    print("-" * 40)
    
    # Check if all models can be instantiated
    models_to_check = [
        Customer, MeasurementProfile, Measurement, GarmentType, 
        StitchingType, Order, OrderItem, Invoice, Payment, 
        Inventory, ExpenseCategory, Expense
    ]
    
    for model in models_to_check:
        try:
            count = model.objects.count()
            print(f"✓ {model.__name__}: {count} records")
        except Exception as e:
            print(f"✗ {model.__name__}: Error - {e}")
    
    # 2. Authentication System
    print("\n2. 🔐 Authentication System")
    print("-" * 40)
    
    # Test login
    response = client.get('/login/')
    if response.status_code == 200:
        print("✓ Login page accessible")
    else:
        print(f"✗ Login page error: {response.status_code}")
    
    # Test admin user
    try:
        admin_user = User.objects.get(username='admin')
        print("✓ Admin user exists")
        
        # Test login
        login_success = client.login(username='admin', password='admin123')
        if login_success:
            print("✓ Admin login successful")
        else:
            print("✗ Admin login failed")
    except User.DoesNotExist:
        print("✗ Admin user not found")
    
    # 3. Main Routes Validation
    print("\n3. 🛣️  Routes Validation")
    print("-" * 40)
    
    routes_to_test = [
        ('dashboard', 'Dashboard'),
        ('customer_list', 'Customer List'),
        ('order_list', 'Order List'),
        ('invoice_list', 'Invoice List'),
        ('payment_list', 'Payment List'),
        ('inventory_list', 'Inventory List'),
        ('quick_billing', 'Quick Billing'),
        ('reports', 'Reports'),
        ('settings', 'Settings'),
    ]
    
    for route_name, display_name in routes_to_test:
        try:
            url = reverse(route_name)
            response = client.get(url)
            if response.status_code in [200, 302]:  # 302 for redirects
                print(f"✓ {display_name}: {response.status_code}")
            else:
                print(f"✗ {display_name}: {response.status_code}")
        except Exception as e:
            print(f"✗ {display_name}: Error - {e}")
    
    # 4. CRUD Operations Validation
    print("\n4. ✏️  CRUD Operations Validation")
    print("-" * 40)
    
    # Test Customer CRUD
    try:
        # Create
        customer = Customer.objects.create(
            name="Test Customer",
            phone="9876543210",
            email="test@example.com",
            address="Test Address"
        )
        print("✓ Customer Create: Success")
        
        # Read
        retrieved_customer = Customer.objects.get(pk=customer.pk)
        print("✓ Customer Read: Success")
        
        # Update
        retrieved_customer.name = "Updated Customer"
        retrieved_customer.save()
        print("✓ Customer Update: Success")
        
        # Delete
        retrieved_customer.delete()
        print("✓ Customer Delete: Success")
        
    except Exception as e:
        print(f"✗ Customer CRUD: Error - {e}")
    
    # 5. API Endpoints Validation
    print("\n5. 🔌 API Endpoints Validation")
    print("-" * 40)
    
    api_endpoints = [
        ('/api/customer-search/?q=test', 'Customer Search API'),
        ('/api/get-price/?garment=1&stitching=1', 'Price Calculation API'),
    ]
    
    for endpoint, name in api_endpoints:
        try:
            response = client.get(endpoint)
            if response.status_code == 200:
                print(f"✓ {name}: {response.status_code}")
            else:
                print(f"✗ {name}: {response.status_code}")
        except Exception as e:
            print(f"✗ {name}: Error - {e}")
    
    # 6. Business Logic Validation
    print("\n6. 🧮 Business Logic Validation")
    print("-" * 40)
    
    # Test order number generation
    try:
        if Order.objects.exists():
            order = Order.objects.first()
            if order.order_number and order.order_number.startswith('ORD-'):
                print("✓ Order number generation: Working")
            else:
                print("✗ Order number generation: Invalid format")
        else:
            print("→ Order number generation: No orders to test")
    except Exception as e:
        print(f"✗ Order number generation: Error - {e}")
    
    # Test invoice number generation
    try:
        if Invoice.objects.exists():
            invoice = Invoice.objects.first()
            if invoice.invoice_number and invoice.invoice_number.startswith('INV-'):
                print("✓ Invoice number generation: Working")
            else:
                print("✗ Invoice number generation: Invalid format")
        else:
            print("→ Invoice number generation: No invoices to test")
    except Exception as e:
        print(f"✗ Invoice number generation: Error - {e}")
    
    # 7. Database Relationships
    print("\n7. 🔗 Database Relationships Validation")
    print("-" * 40)
    
    try:
        # Test foreign key relationships
        if Customer.objects.exists() and Order.objects.exists():
            customer = Customer.objects.first()
            orders = customer.order_set.all()
            print(f"✓ Customer-Order relationship: {orders.count()} orders")
        else:
            print("→ Customer-Order relationship: No data to test")
            
        if Order.objects.exists() and OrderItem.objects.exists():
            order = Order.objects.first()
            items = order.items.all()
            print(f"✓ Order-OrderItem relationship: {items.count()} items")
        else:
            print("→ Order-OrderItem relationship: No data to test")
            
    except Exception as e:
        print(f"✗ Database relationships: Error - {e}")
    
    print("\n" + "="*60)
    print("Validation Complete!")
    print("="*60)
    print("\nIf you see any ✗ errors above, please check:")
    print("1. MySQL server is running")
    print("2. Database 'srijai_tailoring' exists")
    print("3. All migrations have been applied")
    print("4. Initial data has been loaded")
    print("\nTo fix issues, run:")
    print("python setup_mysql.py")
    print("\n")

if __name__ == '__main__':
    validate_all_functionalities()