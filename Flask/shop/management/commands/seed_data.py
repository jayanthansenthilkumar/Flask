"""
Django management command to seed the database with sample data
Run with: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop.models import *
from decimal import Decimal
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    
    def handle(self, *args, **options):
        self.stdout.write('Starting database seeding...')
        
        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('✅ Admin user created: admin/admin123')
        
        # Create staff user if not exists
        if not User.objects.filter(username='staff').exists():
            staff_user = User.objects.create_user('staff', 'staff@example.com', 'staff123')
            staff_user.is_staff = True
            staff_user.save()
            self.stdout.write('✅ Staff user created: staff/staff123')
        
        # Create Garment Types
        garment_types_data = [
            {'name': 'Shirt', 'description': 'Regular shirt', 'base_price': Decimal('500.00')},
            {'name': 'Pants', 'description': 'Regular pants', 'base_price': Decimal('600.00')},
            {'name': 'Suit', 'description': 'Full suit', 'base_price': Decimal('2000.00')},
            {'name': 'Blouse', 'description': 'Ladies blouse', 'base_price': Decimal('400.00')},
            {'name': 'Saree Blouse', 'description': 'Traditional saree blouse', 'base_price': Decimal('300.00')},
        ]
        
        for item in garment_types_data:
            garment, created = GarmentType.objects.get_or_create(
                name=item['name'],
                defaults=item
            )
            if created:
                self.stdout.write(f'✅ Created garment type: {garment.name}')
        
        # Create Stitching Types
        stitching_types_data = [
            {'name': 'Regular', 'description': 'Standard stitching', 'price_multiplier': Decimal('1.0')},
            {'name': 'Premium', 'description': 'High quality stitching', 'price_multiplier': Decimal('1.5')},
            {'name': 'Designer', 'description': 'Designer stitching', 'price_multiplier': Decimal('2.0')},
            {'name': 'Express', 'description': 'Rush order', 'price_multiplier': Decimal('1.3'), 'extra_charge': Decimal('100.00')},
        ]
        
        for item in stitching_types_data:
            stitching, created = StitchingType.objects.get_or_create(
                name=item['name'],
                defaults=item
            )
            if created:
                self.stdout.write(f'✅ Created stitching type: {stitching.name}')
        
        # Create Sample Customers
        customers_data = [
            {'name': 'John Doe', 'phone': '9876543210', 'email': 'john@example.com', 'address': '123 Main St, City'},
            {'name': 'Jane Smith', 'phone': '9876543211', 'email': 'jane@example.com', 'address': '456 Park Ave, City'},
            {'name': 'Bob Wilson', 'phone': '9876543212', 'email': 'bob@example.com', 'address': '789 Oak St, City'},
        ]
        
        for item in customers_data:
            customer, created = Customer.objects.get_or_create(
                phone=item['phone'],
                defaults=item
            )
            if created:
                self.stdout.write(f'✅ Created customer: {customer.name}')
                
                # Create measurement profile for customer
                profile = MeasurementProfile.objects.create(
                    customer=customer,
                    profile_name='Default'
                )
                
                # Add some sample measurements
                measurements_data = [
                    {'measurement_key': 'chest', 'measurement_value': Decimal('40.0'), 'unit': 'inch'},
                    {'measurement_key': 'waist', 'measurement_value': Decimal('34.0'), 'unit': 'inch'},
                    {'measurement_key': 'shoulder', 'measurement_value': Decimal('16.0'), 'unit': 'inch'},
                    {'measurement_key': 'sleeve_length', 'measurement_value': Decimal('24.0'), 'unit': 'inch'},
                ]
                
                for measure in measurements_data:
                    Measurement.objects.create(
                        profile=profile,
                        **measure
                    )
        
        # Create Sample Inventory
        inventory_data = [
            {'item_name': 'Cotton Fabric', 'quantity': Decimal('50.0'), 'unit': 'meters', 'cost_per_unit': Decimal('100.0')},
            {'item_name': 'Silk Fabric', 'quantity': Decimal('25.0'), 'unit': 'meters', 'cost_per_unit': Decimal('200.0')},
            {'item_name': 'Thread Spools', 'quantity': Decimal('100.0'), 'unit': 'pieces', 'cost_per_unit': Decimal('25.0')},
            {'item_name': 'Buttons', 'quantity': Decimal('500.0'), 'unit': 'pieces', 'cost_per_unit': Decimal('2.0')},
        ]
        
        for item in inventory_data:
            inventory, created = Inventory.objects.get_or_create(
                item_name=item['item_name'],
                defaults=item
            )
            if created:
                self.stdout.write(f'✅ Created inventory: {inventory.item_name}')
        
        # Create a sample order
        customer = Customer.objects.first()
        garment = GarmentType.objects.first()
        stitching = StitchingType.objects.first()
        
        if customer and garment and stitching:
            order = Order.objects.create(
                customer=customer,
                delivery_date=date.today() + timedelta(days=7),
                status='PENDING',
                priority='NORMAL',
                notes='Sample order for testing'
            )
            
            OrderItem.objects.create(
                order=order,
                garment_type=garment,
                stitching_type=stitching,
                quantity=1,
                price=garment.base_price * stitching.price_multiplier
            )
            
            self.stdout.write(f'✅ Created sample order: {order.order_number}')
        
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
        self.stdout.write('🎯 You can now login with:')
        self.stdout.write('   Admin: admin/admin123')
        self.stdout.write('   Staff: staff/staff123')