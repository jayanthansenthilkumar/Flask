"""
URL patterns for the shop app
"""
from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Customers
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customers/search/', views.customer_search, name='customer_search'),
    
    # Measurements
    path('customers/<int:customer_id>/measurements/', views.measurement_list, name='measurement_list'),
    path('customers/<int:customer_id>/measurements/add/', views.measurement_add, name='measurement_add'),
    path('measurements/<int:profile_id>/edit/', views.measurement_edit, name='measurement_edit'),
    
    # Orders
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_add, name='order_add'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('orders/<int:pk>/status/', views.order_status_update, name='order_status_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    
    # Quick Billing (main feature)
    path('billing/', views.quick_billing, name='quick_billing'),
    path('billing/create/', views.create_bill, name='create_bill'),
    
    # Invoices
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/print/', views.invoice_print, name='invoice_print'),
    path('orders/<int:order_id>/invoice/create/', views.invoice_create, name='invoice_create'),
    
    # Payments
    path('invoices/<int:invoice_id>/payment/add/', views.payment_add, name='payment_add'),
    path('payments/', views.payment_list, name='payment_list'),
    
    # Inventory
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.inventory_add, name='inventory_add'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),
    
    # Settings
    path('settings/', views.settings_view, name='settings'),
    path('settings/garments/', views.garment_types, name='garment_types'),
    path('settings/stitching/', views.stitching_types, name='stitching_types'),
    
    # Reports
    path('reports/', views.reports, name='reports'),
    path('reports/sales/', views.sales_report, name='sales_report'),
    path('reports/customers/', views.customer_report, name='customer_report'),
    
    # API endpoints for AJAX
    path('api/customer/<int:pk>/', views.api_customer_detail, name='api_customer_detail'),
    path('api/calculate-price/', views.api_calculate_price, name='api_calculate_price'),
    path('api/dashboard-stats/', views.api_dashboard_stats, name='api_dashboard_stats'),
    path('api/customer-search/', views.customer_search, name='api_customer_search'),
    path('api/get-price/', views.api_calculate_price, name='api_get_price'),
    
    # Print endpoints
    path('print/invoice/<int:invoice_id>/', views.print_invoice, name='print_invoice'),
    path('print/receipt/<int:payment_id>/', views.print_receipt, name='print_receipt'),
    path('preview/invoice/<int:invoice_id>/', views.invoice_preview, name='invoice_preview'),
    path('preview/receipt/<int:payment_id>/', views.receipt_preview, name='receipt_preview'),
    
    # User Management
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('users/<int:pk>/toggle/', views.user_toggle_status, name='user_toggle_status'),
]
