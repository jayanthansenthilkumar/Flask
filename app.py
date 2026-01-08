# STUDENT MANAGEMENT SYSTEM - Flask Application for CRUD Operations

from flask import Flask, render_template, request, jsonify
import mysql.connector

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

@app.route('/api/colleges', methods=['GET'])
def get_colleges():
    colleges = [
        "Indian Institute of Technology Delhi",
        "Indian Institute of Technology Bombay",
        "Indian Institute of Technology Madras",
        "Indian Institute of Technology Kanpur",
        "Indian Institute of Technology Kharagpur",
        "Indian Institute of Science Bangalore",
        "Jawaharlal Nehru University",
        "University of Delhi",
        "Anna University",
        "Jadavpur University",
        "Banaras Hindu University",
        "Aligarh Muslim University",
        "National Institute of Technology Trichy",
        "National Institute of Technology Warangal",
        "Vellore Institute of Technology",
        "Birla Institute of Technology and Science Pilani",
        "Manipal Academy of Higher Education",
        "University of Hyderabad",
        "Amity University",
        "SRM Institute of Science and Technology"
    ]
    return jsonify(colleges), 200

@app.route('/api/departments', methods=['GET'])
def get_departments():
    departments = [
        "Computer Science and Engineering",
        "Information Technology",
        "Electronics and Communication Engineering",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Civil Engineering",
        "Chemical Engineering",
        "Biotechnology",
        "Aerospace Engineering",
        "Automobile Engineering",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Business Administration",
        "Commerce",
        "Economics",
        "English Literature",
        "Psychology",
        "Sociology",
        "Political Science"
    ]
    return jsonify(departments), 200

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
        
        email = data.get('email', '').strip()
        if not email:
            email = None
        
        age = data.get('age')
        if not age:
            age = None
        else:
            age = int(age)
        
        phoneno = data.get('phoneno', '').strip()
        if not phoneno:
            phoneno = None
        
        college = data.get('college', '').strip()
        if not college:
            college = None
        
        department = data.get('department', '').strip()
        if not department:
            department = None
        
        insert_query = "INSERT INTO student (name, email, age, phoneno, college, department) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, email, age, phoneno, college, department)
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
            "college": student[5],
            "department": student[6]
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
                "college": student[5] if student[5] else '',
                "department": student[6] if student[6] else ''
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
                "college": student[5] if student[5] else '',
                "department": student[6] if student[6] else ''
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
        
        email = data.get('email', '').strip()
        if not email:
            email = None
        
        age = data.get('age')
        if not age:
            age = None
        else:
            age = int(age)
        
        phoneno = data.get('phoneno', '').strip()
        if not phoneno:
            phoneno = None
        
        college = data.get('college', '').strip()
        if not college:
            college = None
        
        department = data.get('department', '').strip()
        if not department:
            department = None
        
        update_query = "UPDATE student SET name = %s, email = %s, age = %s, phoneno = %s, college = %s, department = %s WHERE id = %s"
        values = (name, email, age, phoneno, college, department, student_id)
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
            "college": student[5] if student[5] else '',
            "department": student[6] if student[6] else ''
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