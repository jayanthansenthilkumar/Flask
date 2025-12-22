#!/bin/bash

# SriJai Tailoring Management System - Database Setup Script
# This script sets up MySQL database and initializes the Django project

echo "========================================================"
echo "SriJai Tailoring Management System - Setup Script"
echo "========================================================"
echo

# Check if MySQL is installed
if ! command -v mysql &> /dev/null; then
    echo "❌ MySQL is not installed. Please install MySQL first."
    echo "   Download from: https://dev.mysql.com/downloads/mysql/"
    echo "   Or use XAMPP/WAMP for Windows"
    exit 1
fi

echo "✅ MySQL found"

# Check if Python virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo "🐍 Virtual environment activated"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Check if MySQL service is running
echo "🔍 Checking MySQL service..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # For Windows (XAMPP)
    if ! tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL; then
        echo "❌ MySQL service is not running."
        echo "   Please start MySQL from XAMPP Control Panel or Services"
        echo "   Or run: net start mysql"
        exit 1
    fi
else
    # For Unix-like systems
    if ! pgrep mysql > /dev/null; then
        echo "❌ MySQL service is not running."
        echo "   Please start MySQL: sudo service mysql start"
        exit 1
    fi
fi

echo "✅ MySQL service is running"

# Run database setup
echo "🗄️  Setting up database..."
python setup_mysql.py

# Check if setup was successful
if [ $? -eq 0 ]; then
    echo
    echo "========================================================"
    echo "✅ Setup completed successfully!"
    echo "========================================================"
    echo
    echo "Next steps:"
    echo "1. Start the development server:"
    echo "   python manage.py runserver"
    echo
    echo "2. Access the application:"
    echo "   http://127.0.0.1:8000/"
    echo
    echo "3. Admin panel:"
    echo "   http://127.0.0.1:8000/admin/"
    echo "   Username: admin"
    echo "   Password: admin123"
    echo
    echo "4. Access phpMyAdmin:"
    echo "   http://localhost/phpmyadmin/"
    echo "   Database: srijai_tailoring"
    echo
    echo "5. Run validation (optional):"
    echo "   python validate_functionality.py"
    echo
else
    echo "❌ Setup failed. Please check the error messages above."
    exit 1
fi