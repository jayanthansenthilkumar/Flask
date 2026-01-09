# STUDENT MANAGEMENT SYSTEM - Flask Application for CRUD Operations

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'  # Change this in production

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'pycrud'

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

def init_db():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        create_db_query = "CREATE DATABASE IF NOT EXISTS " + DB_NAME
        cursor.execute(create_db_query)
        cursor.execute("USE " + DB_NAME)
        
        create_table_query = """
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                age INT,
                phoneno VARCHAR(15),
                state VARCHAR(100),
                city VARCHAR(100),
                college VARCHAR(200),
                department VARCHAR(100)
            )
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Database initialized successfully!")
    except Exception as error:
        print("Error initializing database: " + str(error))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400
    
    username = data['username'].strip()
    password = data['password']
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, username, role FROM users WHERE username = %s AND password = %s", 
                      (username, password))
        user = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[2]
            
            if user[2] == 'admin':
                return jsonify({"success": True, "role": "admin", "redirect": "/adminDashboard"}), 200
            else:
                return jsonify({"success": True, "role": "student", "redirect": "/studentDashboard"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/adminDashboard')
def admin_dashboard():
    if 'user_id' not in session or session.get('role') != 'admin':
        return redirect(url_for('login_page'))
    return render_template('adminDashboard.html')

@app.route('/studentDashboard')
def student_dashboard():
    if 'user_id' not in session or session.get('role') != 'student':
        return redirect(url_for('login_page'))
    return render_template('studentDashboard.html')

@app.route('/students')
def students():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    return render_template('students.html')

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/api/states', methods=['GET'])
def get_states():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name FROM states ORDER BY name ASC")
        states = cursor.fetchall()
        cursor.close()
        connection.close()
        
        result = [state[1] for state in states]
        return jsonify(result), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/cities', methods=['GET'])
def get_cities():
    state = request.args.get('state', '')
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        if state:
            query = """
                SELECT c.name FROM cities c
                JOIN states s ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.name ASC
            """
            cursor.execute(query, (state,))
        else:
            cursor.execute("SELECT DISTINCT name FROM cities ORDER BY name ASC")
        
        cities = cursor.fetchall()
        cursor.close()
        connection.close()
        
        result = [city[0] for city in cities]
        return jsonify(result), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/colleges', methods=['GET'])
def get_colleges():
    state = request.args.get('state', '')
    city = request.args.get('city', '')
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        query = """
            SELECT col.name FROM colleges col
            JOIN states s ON col.state_id = s.id
            JOIN cities c ON col.city_id = c.id
            WHERE 1=1
        """
        params = []
        
        if state:
            query += " AND s.name = %s"
            params.append(state)
        
        if city:
            query += " AND c.name = %s"
            params.append(city)
        
        query += " ORDER BY col.name ASC"
        
        cursor.execute(query, params)
        colleges = cursor.fetchall()
        cursor.close()
        connection.close()
        
        result = [college[0] for college in colleges]
        return jsonify(result), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/departments', methods=['GET'])
def get_departments():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM departments ORDER BY name ASC")
        departments = cursor.fetchall()
        cursor.close()
        connection.close()
        
        result = [dept[0] for dept in departments]
        return jsonify(result), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/departments/short', methods=['GET'])
def get_department_short_names():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, short_name FROM departments ORDER BY name ASC")
        departments = cursor.fetchall()
        cursor.close()
        connection.close()
        
        result = {dept[0]: dept[1] for dept in departments if dept[1]}
        return jsonify(result), 200
    except Exception as error:
        if connection:
            connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    name = data['name'].strip()
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        email = data.get('email', '')
        if email:
            email = email.strip()
        if not email:
            email = None
        
        age = data.get('age')
        if not age:
            age = None
        else:
            age = int(age)
        
        phoneno = data.get('phoneno', '')
        if phoneno:
            phoneno = phoneno.strip()
        if not phoneno:
            phoneno = None
        
        # Get foreign key IDs
        state_id = None
        city_id = None
        college_id = None
        department_id = None
        
        state_name = data.get('state', '')
        if state_name:
            cursor.execute("SELECT id FROM states WHERE name = %s", (state_name,))
            result = cursor.fetchone()
            if result:
                state_id = result[0]
        
        city_name = data.get('city', '')
        if city_name and state_id:
            cursor.execute("SELECT id FROM cities WHERE name = %s AND state_id = %s", (city_name, state_id))
            result = cursor.fetchone()
            if result:
                city_id = result[0]
        
        college_name = data.get('college', '')
        if college_name:
            cursor.execute("SELECT id FROM colleges WHERE name = %s", (college_name,))
            result = cursor.fetchone()
            if result:
                college_id = result[0]
        
        department_name = data.get('department', '')
        if department_name:
            cursor.execute("SELECT id FROM departments WHERE name = %s", (department_name,))
            result = cursor.fetchone()
            if result:
                department_id = result[0]
        
        insert_query = "INSERT INTO student (name, email, age, phoneno, state_id, city_id, college_id, department_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, email, age, phoneno, state_id, city_id, college_id, department_id)
        cursor.execute(insert_query, values)
        connection.commit()
        
        new_id = cursor.lastrowid
        cursor.execute("""
            SELECT s.id, s.name, s.email, s.age, s.phoneno,
                   st.name, c.name, col.name, d.name
            FROM student s
            LEFT JOIN states st ON s.state_id = st.id
            LEFT JOIN cities c ON s.city_id = c.id
            LEFT JOIN colleges col ON s.college_id = col.id
            LEFT JOIN departments d ON s.department_id = d.id
            WHERE s.id = %s
        """, (new_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        response = {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "age": student[3],
            "phoneno": student[4],
            "state": student[5] if student[5] else '',
            "city": student[6] if student[6] else '',
            "college": student[7] if student[7] else '',
            "department": student[8] if student[8] else ''
        }
        
        return jsonify(response), 201
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT s.id, s.name, s.email, s.age, s.phoneno,
                   st.name, c.name, col.name, d.name
            FROM student s
            LEFT JOIN states st ON s.state_id = st.id
            LEFT JOIN cities c ON s.city_id = c.id
            LEFT JOIN colleges col ON s.college_id = col.id
            LEFT JOIN departments d ON s.department_id = d.id
            ORDER BY s.id ASC
        """)
        students_list = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        result = []
        for student in students_list:
            student_data = {
                "id": student[0],
                "name": student[1],
                "email": student[2] if student[2] else '',
                "age": student[3] if student[3] else '',
                "phoneno": student[4] if student[4] else '',
                "state": student[5] if student[5] else '',
                "city": student[6] if student[6] else '',
                "college": student[7] if student[7] else '',
                "department": student[8] if student[8] else ''
            }
            result.append(student_data)
        
        return jsonify(result), 200
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT s.id, s.name, s.email, s.age, s.phoneno,
                   st.name, c.name, col.name, d.name
            FROM student s
            LEFT JOIN states st ON s.state_id = st.id
            LEFT JOIN cities c ON s.city_id = c.id
            LEFT JOIN colleges col ON s.college_id = col.id
            LEFT JOIN departments d ON s.department_id = d.id
            WHERE s.id = %s
        """, (student_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        if student:
            response = {
                "id": student[0],
                "name": student[1],
                "email": student[2] if student[2] else '',
                "age": student[3] if student[3] else '',
                "phoneno": student[4] if student[4] else '',
                "state": student[5] if student[5] else '',
                "city": student[6] if student[6] else '',
                "college": student[7] if student[7] else '',
                "department": student[8] if student[8] else ''
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "Student not found"}), 404
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    name = data['name'].strip()
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400
    
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        email = data.get('email', '')
        if email:
            email = email.strip()
        if not email:
            email = None
        
        age = data.get('age')
        if not age:
            age = None
        else:
            age = int(age)
        
        phoneno = data.get('phoneno', '')
        if phoneno:
            phoneno = phoneno.strip()
        if not phoneno:
            phoneno = None
        
        # Get foreign key IDs
        state_id = None
        city_id = None
        college_id = None
        department_id = None
        
        state_name = data.get('state', '')
        if state_name:
            cursor.execute("SELECT id FROM states WHERE name = %s", (state_name,))
            result = cursor.fetchone()
            if result:
                state_id = result[0]
        
        city_name = data.get('city', '')
        if city_name and state_id:
            cursor.execute("SELECT id FROM cities WHERE name = %s AND state_id = %s", (city_name, state_id))
            result = cursor.fetchone()
            if result:
                city_id = result[0]
        
        college_name = data.get('college', '')
        if college_name:
            cursor.execute("SELECT id FROM colleges WHERE name = %s", (college_name,))
            result = cursor.fetchone()
            if result:
                college_id = result[0]
        
        department_name = data.get('department', '')
        if department_name:
            cursor.execute("SELECT id FROM departments WHERE name = %s", (department_name,))
            result = cursor.fetchone()
            if result:
                department_id = result[0]
        
        update_query = "UPDATE student SET name = %s, email = %s, age = %s, phoneno = %s, state_id = %s, city_id = %s, college_id = %s, department_id = %s WHERE id = %s"
        values = (name, email, age, phoneno, state_id, city_id, college_id, department_id, student_id)
        cursor.execute(update_query, values)
        connection.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404
        
        cursor.execute("""
            SELECT s.id, s.name, s.email, s.age, s.phoneno,
                   st.name, c.name, col.name, d.name
            FROM student s
            LEFT JOIN states st ON s.state_id = st.id
            LEFT JOIN cities c ON s.city_id = c.id
            LEFT JOIN colleges col ON s.college_id = col.id
            LEFT JOIN departments d ON s.department_id = d.id
            WHERE s.id = %s
        """, (student_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        response = {
            "id": student[0],
            "name": student[1],
            "email": student[2] if student[2] else '',
            "age": student[3] if student[3] else '',
            "phoneno": student[4] if student[4] else '',
            "state": student[5] if student[5] else '',
            "city": student[6] if student[6] else '',
            "college": student[7] if student[7] else '',
            "department": student[8] if student[8] else ''
        }
        
        return jsonify(response), 200
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM student WHERE id = %s"
        cursor.execute(delete_query, (student_id,))
        connection.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404
        
        cursor.close()
        connection.close()
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
