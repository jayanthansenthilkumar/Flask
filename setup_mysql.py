"""
MySQL Database Setup Script for SriJai Tailoring Management System
Run this after setting up MySQL and creating the database.
"""
import os
import django
import mysql.connector
from mysql.connector import Error

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
            
    except Error as e:
        print(f"✗ Error creating database: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def setup_django():
    """Setup Django environment and run migrations."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tailor_shop.settings')
    django.setup()
    
    from django.core.management import execute_from_command_line
    from django.contrib.auth import get_user_model
    from shop.models import GarmentType, StitchingType, ExpenseCategory
    
    print("\n" + "="*60)
    print("SriJai Tailoring - MySQL Database Setup")
    print("="*60 + "\n")
    
    # Create database
    create_database()
    
    # Run migrations
    print("\n📦 Running database migrations...")
    execute_from_command_line(['manage.py', 'makemigrations', 'shop'])
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create superuser
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
    
    # Create initial data
    create_initial_data()
    
    print("\n" + "="*60)
    print("Setup Complete!")
    print("="*60)
    print("\nYou can now:")
    print("1. Run the server: python manage.py runserver")
    print("2. Access admin: http://localhost:8000/admin/")
    print("3. Login with: admin / admin123")
    print("4. Access phpMyAdmin to view database")
    print("\nMySQL Database: srijai")
    print("Tables will be prefixed with 'shop_'")
    print("\n")

def create_initial_data():
    """Create initial garment types, stitching types, and expense categories."""
    from shop.models import GarmentType, StitchingType, ExpenseCategory
    
    # Garment types
    garments = [
        ('Shirt', 'Men\'s formal and casual shirts', 450),
        ('Pant', 'Men\'s formal and casual pants/trousers', 500),
        ('Kurta', 'Traditional Indian kurta', 550),
        ('Blouse', 'Women\'s saree blouse', 400),
        ('Salwar Kameez', 'Women\'s salwar suit set', 800),
        ('Suit (2-Piece)', 'Men\'s formal 2-piece suit', 3500),
        ('Suit (3-Piece)', 'Men\'s formal 3-piece suit with waistcoat', 5000),
        ('Lehenga', 'Traditional lehenga for women', 2500),
        ('Sherwani', 'Traditional men\'s wedding wear', 4500),
        ('Churidar', 'Fitted pants worn with kurta', 350),
    ]
    
    created_garments = 0
    for name, description, price in garments:
        obj, created = GarmentType.objects.get_or_create(
            name=name,
            defaults={'description': description, 'base_price': price}
        )
        if created:
            created_garments += 1
    
    print(f"✓ Garment types: {created_garments} created, {len(garments) - created_garments} already exist")
    
    # Stitching types
    stitching = [
        ('Regular', 'Standard stitching quality', 0),
        ('Premium', 'High quality stitching with better finish', 150),
        ('Designer', 'Designer stitching with special patterns', 350),
        ('Express', 'Quick delivery with standard quality', 200),
        ('Hand Embroidery', 'Traditional hand embroidery work', 500),
    ]
    
    created_stitching = 0
    for name, description, extra in stitching:
        obj, created = StitchingType.objects.get_or_create(
            name=name,
            defaults={'description': description, 'extra_charge': extra}
        )
        if created:
            created_stitching += 1
    
    print(f"✓ Stitching types: {created_stitching} created, {len(stitching) - created_stitching} already exist")
    
    # Expense categories
    categories = [
        ('Materials', 'Thread, buttons, zippers, etc.'),
        ('Utilities', 'Electricity, water bills'),
        ('Rent', 'Shop rent and maintenance'),
        ('Salaries', 'Employee wages and salaries'),
        ('Equipment', 'Sewing machines, irons, etc.'),
        ('Transportation', 'Delivery and pickup expenses'),
        ('Miscellaneous', 'Other expenses'),
    ]
    
    created_categories = 0
    for name, description in categories:
        obj, created = ExpenseCategory.objects.get_or_create(
            name=name,
            defaults={'description': description}
        )
        if created:
            created_categories += 1
    
    print(f"✓ Expense categories: {created_categories} created, {len(categories) - created_categories} already exist")

if __name__ == '__main__':
    setup_django()