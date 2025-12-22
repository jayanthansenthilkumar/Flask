#!/usr/bin/env python
"""
SriJai Tailoring Management System - Complete Setup
Clean setup for immediate use with all features
"""
import os
import django
from django.core.management import execute_from_command_line

def main():
    """Main setup function."""
    print("\n" + "="*60)
    print("🏷️ SriJai Tailoring - Complete Setup & Cleanup")
    print("="*60 + "\n")
    
    # Set Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tailor_shop.settings')
    django.setup()
    
    print("📦 Setting up database...")
    
    # Run migrations
    try:
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("✓ Database migrations completed")
    except Exception as e:
        print(f"❌ Migration error: {e}")
        return
    
    # Create superuser
    print("👤 Creating admin user...")
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser(
                username='admin',
                email='admin@srijai.com',
                password='admin123',
                first_name='Admin',
                last_name='User',
            )
            print("✓ Admin user created (admin/admin123)")
        else:
            print("✓ Admin user already exists")
            
        # Create a staff user for billing
        if not User.objects.filter(username='staff').exists():
            staff_user = User.objects.create_user(
                username='staff',
                email='staff@srijai.com',
                password='staff123',
                first_name='Staff',
                last_name='User',
                is_staff=True,
            )
            print("✓ Staff user created (staff/staff123)")
        else:
            print("✓ Staff user already exists")
    except Exception as e:
        print(f"❌ Error creating admin: {e}")
    
    # Create initial data
    print("📋 Loading initial data...")
    try:
        from shop.models import GarmentType, StitchingType, ExpenseCategory
        
        # Create garment types
        garment_data = [
            {'name': 'Shirt', 'base_price': 500.00, 'description': 'Regular shirt'},
            {'name': 'Pant', 'base_price': 400.00, 'description': 'Regular pant'},
            {'name': 'Suit', 'base_price': 1500.00, 'description': 'Full suit'},
            {'name': 'Blouse', 'base_price': 600.00, 'description': 'Ladies blouse'},
            {'name': 'Dress', 'base_price': 800.00, 'description': 'Ladies dress'},
            {'name': 'Kurta', 'base_price': 700.00, 'description': 'Traditional kurta'},
            {'name': 'Saree Blouse', 'base_price': 650.00, 'description': 'Saree blouse'},
            {'name': 'Lehenga', 'base_price': 2000.00, 'description': 'Traditional lehenga'},
            {'name': 'Coat', 'base_price': 1200.00, 'description': 'Formal coat'},
            {'name': 'Churidar', 'base_price': 550.00, 'description': 'Traditional churidar'},
        ]
        
        for item in garment_data:
            obj, created = GarmentType.objects.get_or_create(name=item['name'], defaults=item)
            if created:
                print(f"   ✓ {item['name']} garment type")
        
        # Create stitching types
        stitching_data = [
            {'name': 'Regular', 'price_multiplier': 1.0, 'description': 'Regular stitching'},
            {'name': 'Premium', 'price_multiplier': 1.5, 'description': 'Premium quality'},
            {'name': 'Designer', 'price_multiplier': 2.0, 'description': 'Designer with embellishments'},
            {'name': 'Express', 'price_multiplier': 1.3, 'description': 'Express delivery'},
            {'name': 'Economy', 'price_multiplier': 0.8, 'description': 'Budget-friendly'},
        ]
        
        for item in stitching_data:
            obj, created = StitchingType.objects.get_or_create(name=item['name'], defaults=item)
            if created:
                print(f"   ✓ {item['name']} stitching type")
        
        # Create expense categories
        expense_data = [
            {'name': 'Materials', 'description': 'Fabric, buttons, zippers'},
            {'name': 'Equipment', 'description': 'Sewing machines, tools'},
            {'name': 'Rent', 'description': 'Shop rent and utilities'},
            {'name': 'Salary', 'description': 'Staff salaries'},
            {'name': 'Marketing', 'description': 'Advertising and promotion'},
            {'name': 'Transportation', 'description': 'Delivery costs'},
            {'name': 'Miscellaneous', 'description': 'Other expenses'},
        ]
        
        for item in expense_data:
            obj, created = ExpenseCategory.objects.get_or_create(name=item['name'], defaults=item)
            if created:
                print(f"   ✓ {item['name']} expense category")
        
        print("✓ Initial data loaded successfully")
        
    except Exception as e:
        print(f"❌ Error loading initial data: {e}")
    
    # Collect static files
    print("📦 Collecting static files...")
    try:
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
        print("✓ Static files collected")
    except Exception as e:
        print(f"⚠️ Static files warning: {e}")
    
    print("\n" + "="*60)
    print("🎉 SriJai Tailoring Setup Complete!")
    print("="*60)
    
    print("\n✅ System Ready:")
    print("   📊 Database: SQLite (db.sqlite3)")
    print("   👤 Admin User: admin / admin123") 
    print("   👤 Staff User: staff / staff123") 
    print("   🏷️ Shop Name: SriJai Tailoring")
    print("   📦 10 Garment Types loaded")
    print("   ✂️ 5 Stitching Types loaded")
    print("   💰 7 Expense Categories loaded")
    print("   🖨️ PDF Receipt/Invoice Printing")
    
    print("\n🚀 Start Application:")
    print("   1. python manage.py runserver")
    print("   2. Open: http://127.0.0.1:8000/")
    print("   3. Login: http://127.0.0.1:8000/login/ (staff/staff123)")
    print("   4. Admin: http://127.0.0.1:8000/admin/ (admin/admin123)")
    print("   5. Billing: http://127.0.0.1:8000/billing/ (after login)")
    
    print("\n💡 New Features:")
    print("   • PDF Invoice Generation")
    print("   • PDF Receipt Printing") 
    print("   • Invoice Preview & Download")
    print("   • Payment Receipt Management")
    print("   • Clean & Optimized Backend")
    print("   • Automatic Number Generation")
    
    print("\n📝 Note: For MySQL, upgrade to MariaDB 10.6+ first")
    print("   Database name configured: 'srijai'")
    print()

if __name__ == "__main__":
    main()