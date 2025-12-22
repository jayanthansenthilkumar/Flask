"""
Setup script for TailorShop Management System
Run this after setting up Django to create initial data.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tailor_shop.settings')
django.setup()

from django.contrib.auth import get_user_model
from shop.models import GarmentType, StitchingType, ExpenseCategory

def create_superuser():
    """Create admin superuser if not exists."""
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_superuser(
            username='admin',
            email='admin@tailorshop.com',
            password='admin123',
            first_name='Admin',
            last_name='User',
        )
        # Set role if the model supports it
        if hasattr(user, 'role'):
            user.role = 'ADMIN'
            user.save()
        print("✓ Superuser 'admin' created (password: admin123)")
    else:
        print("→ Superuser 'admin' already exists")

def create_garment_types():
    """Create default garment types."""
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
    
    created_count = 0
    for name, description, price in garments:
        obj, created = GarmentType.objects.get_or_create(
            name=name,
            defaults={'description': description, 'base_price': price}
        )
        if created:
            created_count += 1
    
    print(f"✓ Garment types: {created_count} created, {len(garments) - created_count} already exist")

def create_stitching_types():
    """Create default stitching types."""
    stitching = [
        ('Regular', 'Standard stitching quality', 0),
        ('Premium', 'High quality stitching with better finish', 150),
        ('Designer', 'Designer stitching with special patterns', 350),
        ('Express', 'Quick delivery with standard quality', 200),
        ('Hand Embroidery', 'Traditional hand embroidery work', 500),
    ]
    
    created_count = 0
    for name, description, extra in stitching:
        obj, created = StitchingType.objects.get_or_create(
            name=name,
            defaults={'description': description, 'extra_charge': extra}
        )
        if created:
            created_count += 1
    
    print(f"✓ Stitching types: {created_count} created, {len(stitching) - created_count} already exist")

def create_expense_categories():
    """Create default expense categories."""
    categories = [
        ('Materials', 'Thread, buttons, zippers, etc.'),
        ('Utilities', 'Electricity, water bills'),
        ('Rent', 'Shop rent and maintenance'),
        ('Salaries', 'Employee wages and salaries'),
        ('Equipment', 'Sewing machines, irons, etc.'),
        ('Transportation', 'Delivery and pickup expenses'),
        ('Miscellaneous', 'Other expenses'),
    ]
    
    created_count = 0
    for name, description in categories:
        obj, created = ExpenseCategory.objects.get_or_create(
            name=name,
            defaults={'description': description}
        )
        if created:
            created_count += 1
    
    print(f"✓ Expense categories: {created_count} created, {len(categories) - created_count} already exist")

def main():
    print("\n" + "="*50)
    print("TailorShop - Initial Setup")
    print("="*50 + "\n")
    
    create_superuser()
    create_garment_types()
    create_stitching_types()
    create_expense_categories()
    
    print("\n" + "="*50)
    print("Setup Complete!")
    print("="*50)
    print("\nYou can now:")
    print("1. Run the server: python manage.py runserver")
    print("2. Access admin: http://localhost:8000/admin/")
    print("3. Login with: admin / admin123")
    print("\n")

if __name__ == '__main__':
    main()
