# QUESTION PAPER STORAGE SYSTEM - Flask Application for CRUD Operations

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
import mysql.connector
from data import DEPARTMENTS, YEARS, SUBJECTS_BY_DEPARTMENT

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'pycrud'

# Session management decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_page'))
        if session.get('role') != 'admin':
            return redirect(url_for('student_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def student_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_page'))
        if session.get('role') != 'student':
            return redirect(url_for('admin_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Exception as error:
        print("Error connecting to database: " + str(error))
        return None

@app.route('/')
def home():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif session.get('role') == 'student':
            return redirect(url_for('student_dashboard'))
    return render_template('index.html')

@app.route('/login')
def login_page():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin_dashboard'))
        elif session.get('role') == 'student':
            return redirect(url_for('student_dashboard'))
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400
    
    username = data['username'].strip()
    password = data['password']
    role = data.get('role', 'student')
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, username, role FROM users WHERE username = %s AND password = %s AND role = %s", 
                      (username, password, role))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user:
            session.clear()
            session.permanent = True
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[2]
            
            if user[2] == 'admin':
                return jsonify({"success": True, "role": "admin", "redirect": "/adminDashboard"}), 200
            else:
                return jsonify({"success": True, "role": "student", "redirect": "/studentDashboard"}), 200
        else:
            return jsonify({"error": "Invalid credentials or incorrect role"}), 401
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/adminDashboard')
@admin_required
def admin_dashboard():
    return render_template('adminDashboard.html', username=session.get('username'))

@app.route('/studentDashboard')
@student_required
def student_dashboard():
    return render_template('studentDashboard.html', username=session.get('username'))

@app.route('/papers')
@login_required
def papers():
    return render_template('papers.html', username=session.get('username'), role=session.get('role'))

@app.route('/api/static-data', methods=['GET'])
def get_static_data():
    return jsonify({
        "departments": DEPARTMENTS,
        "years": YEARS,
        "subjects": SUBJECTS_BY_DEPARTMENT
    })

@app.route('/api/papers', methods=['GET'])
@login_required
def get_papers():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        department_filter = request.args.get('department')
        year_filter = request.args.get('year')
        subject_filter = request.args.get('subject')
        
        query = "SELECT id, title, department, subject, year, link, created_at FROM question_papers WHERE 1=1"
        params = []
        
        if department_filter:
            query += " AND department = %s"
            params.append(department_filter)
        if year_filter:
            query += " AND year = %s"
            params.append(year_filter)
        if subject_filter:
            query += " AND subject = %s"
            params.append(subject_filter)
            
        query += " ORDER BY created_at DESC"
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, tuple(params))
        result = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return jsonify(result), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/papers', methods=['POST'])
@admin_required
def add_paper():
    data = request.get_json()
    
    required_fields = ['title', 'department', 'subject', 'year', 'link']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
        
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
        
    try:
        cursor = connection.cursor()
        query = """INSERT INTO question_papers (title, department, subject, year, link) 
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (data['title'], data['department'], data['subject'], data['year'], data['link']))
        connection.commit()
        
        paper_id = cursor.lastrowid
        cursor.close()
        connection.close()
        
        return jsonify({"success": True, "message": "Question paper added successfully", "id": paper_id}), 201
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/papers/<int:id>', methods=['PUT'])
@admin_required
def update_paper(id):
    data = request.get_json()
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
        
    try:
        cursor = connection.cursor()
        
        # Check if exists
        cursor.execute("SELECT id FROM question_papers WHERE id = %s", (id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return jsonify({"error": "Paper not found"}), 404
            
        # Update
        query = """UPDATE question_papers 
                   SET title=%s, department=%s, subject=%s, year=%s, link=%s 
                   WHERE id=%s"""
        cursor.execute(query, (data['title'], data['department'], data['subject'], data['year'], data['link'], id))
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return jsonify({"success": True, "message": "Paper updated successfully"}), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/papers/<int:id>', methods=['DELETE'])
@admin_required
def delete_paper(id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
        
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM question_papers WHERE id = %s", (id,))
        connection.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Paper not found"}), 404
            
        cursor.close()
        connection.close()
        
        return jsonify({"success": True, "message": "Paper deleted successfully"}), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/dashboard/stats')
@login_required
def dashboard_stats():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
        
    try:
        cursor = connection.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM question_papers")
        total_papers = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT subject) FROM question_papers")
        total_subjects = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT year) FROM question_papers")
        total_years = cursor.fetchone()[0]
        
        cursor.close()
        connection.close()
        
        return jsonify({
            "total_papers": total_papers,
            "total_subjects": total_subjects,
            "total_years": total_years
        }), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
