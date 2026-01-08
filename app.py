# STUDENT MANAGEMENT SYSTEM - Flask Application for CRUD Operations

from flask import Flask, render_template, request, jsonify
import mysql.connector
from data import STATES, CITIES_BY_STATE, COLLEGES, DEPARTMENTS, DEPARTMENT_SHORT_NAMES

app = Flask(__name__)

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

@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/api/states', methods=['GET'])
def get_states():
    return jsonify(STATES), 200

@app.route('/api/cities', methods=['GET'])
def get_cities():
    state = request.args.get('state', '')
    
    if state and state in CITIES_BY_STATE:
        return jsonify(CITIES_BY_STATE[state]), 200
    else:
        all_cities = []
        for city_list in CITIES_BY_STATE.values():
            all_cities.extend(city_list)
        return jsonify(sorted(set(all_cities))), 200

@app.route('/api/colleges', methods=['GET'])
def get_colleges():
    state = request.args.get('state', '')
    city = request.args.get('city', '')
    
    filtered_colleges = COLLEGES
    
    if state:
        filtered_colleges = [c for c in filtered_colleges if c["state"] == state]
    
    if city:
        filtered_colleges = [c for c in filtered_colleges if c["city"] == city]
    
    college_names = [c["name"] for c in filtered_colleges]
    
    return jsonify(college_names), 200

@app.route('/api/departments', methods=['GET'])
def get_departments():
    return jsonify(DEPARTMENTS), 200

@app.route('/api/departments/short', methods=['GET'])
def get_department_short_names():
    return jsonify(DEPARTMENT_SHORT_NAMES), 200

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
        
        state = data.get('state', '')
        if state:
            state = state.strip()
        if not state:
            state = None
        
        city = data.get('city', '')
        if city:
            city = city.strip()
        if not city:
            city = None
        
        college = data.get('college', '')
        if college:
            college = college.strip()
        if not college:
            college = None
        
        department = data.get('department', '')
        if department:
            department = department.strip()
        if not department:
            department = None
        
        insert_query = "INSERT INTO student (name, email, age, phoneno, state, city, college, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, email, age, phoneno, state, city, college, department)
        cursor.execute(insert_query, values)
        connection.commit()
        
        new_id = cursor.lastrowid
        cursor.execute("SELECT * FROM student WHERE id = %s", (new_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        response = {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "age": student[3],
            "phoneno": student[4],
            "state": student[5],
            "city": student[6],
            "college": student[7],
            "department": student[8]
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
        cursor.execute("SELECT * FROM student ORDER BY id ASC")
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
        cursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
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
        
        state = data.get('state', '')
        if state:
            state = state.strip()
        if not state:
            state = None
        
        city = data.get('city', '')
        if city:
            city = city.strip()
        if not city:
            city = None
        
        college = data.get('college', '')
        if college:
            college = college.strip()
        if not college:
            college = None
        
        department = data.get('department', '')
        if department:
            department = department.strip()
        if not department:
            department = None
        
        update_query = "UPDATE student SET name = %s, email = %s, age = %s, phoneno = %s, state = %s, city = %s, college = %s, department = %s WHERE id = %s"
        values = (name, email, age, phoneno, state, city, college, department, student_id)
        cursor.execute(update_query, values)
        connection.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404
        
        cursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
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
