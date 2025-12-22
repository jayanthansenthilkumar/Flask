#!/usr/bin/env python
"""
Enhanced MySQL Database Setup Script for SriJai Tailoring Management System
Handles version compatibility issues and provides fallback options
"""
import os
import sys
import mysql.connector
from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Update this with your MySQL password
    'database': 'srijai'
}

def create_database():
    """Create the database if it doesn't exist."""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"✓ Database '{DB_CONFIG['database']}' created successfully")
            connection.commit()
    
    except mysql.connector.Error as err:
        print(f"❌ Error creating database: {err}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
    return True

def setup_django_with_fallback():
    """Setup Django with fallback to SQLite if MySQL version issues."""
    import django
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tailor_shop.settings')
    
    try:
        # Try MySQL first
        django.setup()
        print("📦 Running database migrations with MySQL...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("✓ MySQL database setup completed")
        return True
        
    except Exception as e:
        if "MariaDB" in str(e) or "not supported" in str(e):
            print(f"⚠️ MySQL/MariaDB version compatibility issue: {e}")
            print("📝 Switching to SQLite for better compatibility...")
            
            # Update settings to use SQLite
            settings_path = 'tailor_shop/settings.py'
            with open(settings_path, 'r') as f:
                content = f.read()
            
            # Switch to SQLite in settings
            updated_content = content.replace(
                "# Database - MySQL Configuration",
                "# Database - MySQL Configuration (disabled due to version compatibility)"
            ).replace(
                "DATABASES = {",
                "# DATABASES = {"
            ).replace(
                "# SQLite fallback",
                "# SQLite Configuration (active)"
            ).replace(
                "# DATABASES = {\n#     'default': {\n#         'ENGINE': 'django.db.backends.sqlite3',\n#         'NAME': BASE_DIR / 'db.sqlite3',\n#     }\n# }",
                "DATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.sqlite3',\n        'NAME': BASE_DIR / 'db.sqlite3',\n    }\n}"
            )
            
            with open(settings_path, 'w') as f:
                f.write(updated_content)
            
            # Reload Django with SQLite
            django.setup()
            execute_from_command_line(['manage.py', 'makemigrations'])
            execute_from_command_line(['manage.py', 'migrate'])
            print("✓ SQLite database setup completed")
            return False  # MySQL not used
        else:
            raise e

def create_superuser():
    """Create admin superuser."""
    try:
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser(
                username='admin',
                email='admin@srijai.com',
                password='admin123',
                first_name='Admin',
                last_name='User',
            )
            print("✓ Superuser 'admin' created (password: admin123)")
        else:
            print("→ Superuser 'admin' already exists")
    except Exception as e:
        print(f"❌ Error creating superuser: {e}")

def create_initial_data():
    """Create initial data for the application."""
    try:
        from shop.models import GarmentType, StitchingType, ExpenseCategory
        
        # Create garment types
        garment_types = [
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
        
        for gt_data in garment_types:
            gt, created = GarmentType.objects.get_or_create(
                name=gt_data['name'],
                defaults=gt_data
            )
            if created:
                print(f"✓ Created garment type: {gt.name}")
        
        # Create stitching types
        stitching_types = [
            {'name': 'Regular', 'price_multiplier': 1.0, 'description': 'Regular stitching'},
            {'name': 'Premium', 'price_multiplier': 1.5, 'description': 'Premium quality stitching'},
            {'name': 'Designer', 'price_multiplier': 2.0, 'description': 'Designer stitching with embellishments'},
            {'name': 'Express', 'price_multiplier': 1.3, 'description': 'Express delivery stitching'},
            {'name': 'Economy', 'price_multiplier': 0.8, 'description': 'Budget-friendly stitching'},
        ]
        
        for st_data in stitching_types:
            st, created = StitchingType.objects.get_or_create(
                name=st_data['name'],
                defaults=st_data
            )
            if created:
                print(f"✓ Created stitching type: {st.name}")
        
        # Create expense categories
        expense_categories = [
            {'name': 'Materials', 'description': 'Fabric, buttons, zippers, etc.'},
            {'name': 'Equipment', 'description': 'Sewing machines, tools, etc.'},
            {'name': 'Rent', 'description': 'Shop rent and utilities'},
            {'name': 'Salary', 'description': 'Staff salaries'},
            {'name': 'Marketing', 'description': 'Advertising and promotion'},
            {'name': 'Transportation', 'description': 'Delivery and pickup costs'},
            {'name': 'Miscellaneous', 'description': 'Other business expenses'},
        ]
        
        for ec_data in expense_categories:
            ec, created = ExpenseCategory.objects.get_or_create(
                name=ec_data['name'],
                defaults=ec_data
            )
            if created:
                print(f"✓ Created expense category: {ec.name}")
                
    except Exception as e:
        print(f"❌ Error creating initial data: {e}")

def main():
    """Main setup function."""
    print("\n" + "="*60)
    print("SriJai Tailoring - Enhanced Database Setup")
    print("="*60 + "\n")
    
    # Check if MySQL is available and create database
    mysql_available = False
    if create_database():
        mysql_available = True
    
    # Setup Django with fallback
    mysql_used = setup_django_with_fallback()
    
    # Create superuser
    create_superuser()
    
    # Create initial data
    print("\n📋 Loading initial data...")
    create_initial_data()
    
    print("\n" + "="*60)
    print("🎉 Setup Complete!")
    print("="*60)
    print("\n✅ System Status:")
    if mysql_used:
        print("   Database: MySQL (srijai)")
        print("   phpMyAdmin: http://localhost/phpmyadmin/")
    else:
        print("   Database: SQLite (db.sqlite3)")
        print("   Note: MySQL available but version compatibility issue")
    
    print("\n🚀 Next Steps:")
    print("1. Start server: python manage.py runserver")
    print("2. Open browser: http://localhost:8000/")
    print("3. Admin panel: http://localhost:8000/admin/")
    print("4. Login: admin / admin123")
    print("\n")

if __name__ == "__main__":
    main()