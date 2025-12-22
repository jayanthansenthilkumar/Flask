# TailorShop Management System

A complete Django-based Tailoring Shop Management System with automated billing, customer management, order tracking, and comprehensive reporting.

## Features

- 👤 **Customer Management** - Add, edit, and track customers with their measurements
- 📏 **Measurement Profiles** - Store multiple measurement profiles per customer
- 📋 **Order Management** - Create and track orders with multiple items
- ⚡ **Quick Billing** - Fast billing interface with customer search and auto-calculation
- 🧾 **Invoice Generation** - Automatic invoice creation with discounts support
- 💰 **Payment Tracking** - Track payments with multiple payment modes (Cash, UPI, Card, Bank)
- 📦 **Inventory Management** - Track materials and supplies with low-stock alerts
- 📊 **Reports** - Sales reports, customer reports, and payment history
- 🎨 **Attractive UI** - Modern, responsive interface with Bootstrap 5

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5.3
- **Icons**: Bootstrap Icons
- **Database**: SQLite (easily switchable to PostgreSQL)

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone/Navigate to the project directory**
   ```bash
   cd Taior
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Setup initial data (creates admin user and default data)**
   ```bash
   python setup_initial_data.py
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main App: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - Login: `admin` / `admin123`

## Project Structure

```
Taior/
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── setup_initial_data.py       # Initial data setup script
├── README.md                   # This file
│
├── tailor_shop/               # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── shop/                      # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # URL routing
│   ├── forms.py               # Django forms
│   ├── admin.py               # Admin configuration
│   └── fixtures/              # Initial data fixtures
│
├── templates/                 # HTML templates
│   ├── base.html              # Base template with sidebar
│   └── shop/                  # App-specific templates
│       ├── dashboard.html
│       ├── customer_*.html
│       ├── order_*.html
│       ├── invoice_*.html
│       ├── quick_billing.html
│       └── ...
│
└── static/                    # Static files
    ├── css/
    │   └── style.css          # Custom styles
    └── js/
        ├── main.js            # Utility functions
        └── quick-billing.js   # Billing automation
```

## Usage Guide

### Quick Billing (Main Feature)

1. Navigate to **Billing** > **Quick Billing**
2. Search for existing customer or add new
3. Add items to the order
4. Apply discounts if needed
5. Record payment
6. Generate invoice automatically

### Customer Management

1. Go to **Customers** section
2. Add new customers with contact details
3. Add measurement profiles for each garment type
4. View customer order history

### Order Management

1. Create orders from **Orders** > **New Order**
2. Track order status (Pending → In Progress → Ready → Delivered)
3. Set priority levels (Normal, Urgent, Express)
4. View and print order details

### Reports

1. **Sales Report** - View sales by date range, payment mode breakdown
2. **Customer Report** - Top customers, pending payments
3. **Payment History** - All payment transactions

## Customization

### Adding New Garment Types

1. Go to Admin Panel or **Settings** > **Garment Types**
2. Add new garment with base price

### Adding New Stitching Types

1. Go to **Settings** > **Stitching Types**
2. Add stitching type with price modifier

### Switching to PostgreSQL

1. Install PostgreSQL and create a database
2. Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'tailorshop',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
3. Run migrations: `python manage.py migrate`

## API Endpoints

The system includes some internal API endpoints for AJAX functionality:

- `GET /api/customer-search/?q=<query>` - Search customers
- `GET /api/get-price/?garment=<id>&stitching=<id>` - Get price calculation
- `POST /api/create-bill/` - Create complete bill

## License

This project is for educational and commercial use. Feel free to modify and use it for your tailoring business.

## Support

For any issues or feature requests, please create an issue in the repository.

---

Made with ❤️ for Tailoring Shop Owners
