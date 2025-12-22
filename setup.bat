@echo off
REM SriJai Tailoring Management System - Windows Setup Script
REM This script sets up MySQL database and initializes the Django project

echo ========================================================
echo SriJai Tailoring Management System - Setup Script
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python first.
    echo    Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Python found

REM Check if MySQL is available (XAMPP)
if not exist "C:\xampp\mysql\bin\mysql.exe" (
    if not exist "C:\Program Files\MySQL\MySQL Server*\bin\mysql.exe" (
        echo ❌ MySQL not found. Please install MySQL or XAMPP.
        echo    XAMPP Download: https://www.apachefriends.org/
        echo    MySQL Download: https://dev.mysql.com/downloads/mysql/
        pause
        exit /b 1
    )
)
echo ✅ MySQL found

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🐍 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install Python dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

REM Check if MySQL service is running
echo 🔍 Checking MySQL service...
tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
if errorlevel 1 (
    echo ❌ MySQL service is not running.
    echo    Please start MySQL from XAMPP Control Panel
    echo    Or start the MySQL service from Windows Services
    pause
    exit /b 1
)
echo ✅ MySQL service is running

REM Run database setup
echo 🗄️  Setting up database...
python setup_mysql.py

if errorlevel 1 (
    echo ❌ Setup failed. Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo ✅ Setup completed successfully!
echo ========================================================
echo.
echo Next steps:
echo 1. Start the development server:
echo    python manage.py runserver
echo.
echo 2. Access the application:
echo    http://127.0.0.1:8000/
echo.
echo 3. Admin panel:
echo    http://127.0.0.1:8000/admin/
echo    Username: admin
echo    Password: admin123
echo.
echo 4. Access phpMyAdmin:
echo    http://localhost/phpmyadmin/
echo    Database: srijai_tailoring
echo.
echo 5. Run validation (optional):
echo    python validate_functionality.py
echo.

pause