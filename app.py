# Import required libraries
from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime

# Create Flask app
app = Flask(__name__)

# MySQL Database Configuration - Change password before running
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''  # CHANGE THIS to your MySQL password
DB_NAME = 'pycrud'


# Function to connect to MySQL database
def get_db_connection():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Exception as error:
        print("Error connecting to MySQL: " + str(error))
        return None


# Function to setup database and create student table
def init_db():
    try:
        # First connect without database name
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS " + DB_NAME
        cursor.execute(create_db_query)
        
        # Use the database
        use_db_query = "USE " + DB_NAME
        cursor.execute(use_db_query)
        
        # Create student table if it doesn't exist
        create_table_query = """
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                age INT,
                course VARCHAR(100)
            )
        """
        cursor.execute(create_table_query)
        
        # Save changes
        connection.commit()
        cursor.close()
        connection.close()
        print("Database and table created successfully!")
        
    except Exception as error:
        print("Error creating database: " + str(error))


# Home page route - show dashboard
@app.route('/')
def home():
    return render_template('index.html')


# Students page route
@app.route('/students')
def students():
    return render_template('students.html')


# Health check route
@app.route('/api/health')
def health():
    response = {"status": "ok"}
    return jsonify(response), 200


# CREATE - Add new student to database
@app.route('/api/students', methods=['POST'])
def create_student():
    # Get data from request
    data = request.get_json()
    
    # Check if name is provided
    if not data:
        error_response = {"error": "No data provided"}
        return jsonify(error_response), 400
    
    if 'name' not in data:
        error_response = {"error": "Name is required"}
        return jsonify(error_response), 400
    
    student_name = data['name'].strip()
    if not student_name:
        error_response = {"error": "Name cannot be empty"}
        return jsonify(error_response), 400
    
    # Get database connection
    connection = get_db_connection()
    if not connection:
        error_response = {"error": "Database connection failed"}
        return jsonify(error_response), 500
    
    try:
        cursor = connection.cursor()
        
        # Prepare student data
        student_email = data.get('email', '').strip()
        if not student_email:
            student_email = None
            
        student_age = data.get('age')
        if not student_age:
            student_age = None
            
        student_course = data.get('course', '').strip()
        if not student_course:
            student_course = None
        
        # Insert query
        insert_query = "INSERT INTO student (name, email, age, course) VALUES (%s, %s, %s, %s)"
        values = (student_name, student_email, student_age, student_course)
        
        # Execute insert
        cursor.execute(insert_query, values)
        connection.commit()
        
        # Get the ID of newly created student
        new_student_id = cursor.lastrowid
        
        # Fetch the newly created student
        select_query = "SELECT * FROM student WHERE id = %s"
        cursor.execute(select_query, (new_student_id,))
        student = cursor.fetchone()
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        # Prepare response
        created_at = student[5].strftime("%Y-%m-%d %H:%M:%S")
        response = {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "age": student[3],
            "course": student[4]
        }
        
        return jsonify(response), 201
        
    except Exception as error:
        error_response = {"error": str(error)}
        return jsonify(error_response), 500


# READ - Get all students from database
@app.route('/api/students', methods=['GET'])
def get_students():
    # Get database connection
    connection = get_db_connection()
    if not connection:
        error_response = {"error": "Database connection failed"}
        return jsonify(error_response), 500
    
    try:
        cursor = connection.cursor()
        
        # Select all students
        select_query = "SELECT * FROM student ORDER BY id DESC"
        cursor.execute(select_query)
        students = cursor.fetchall()
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        # Prepare list of students
        result = []
        for student in students:
            # Handle empty values
            student_email = student[2]
            if not student_email:
                student_email = ''
                
            student_age = student[3]
            if not student_age:
                student_age = ''
                
            student_course = student[4]
            if not student_course:
                student_course = ''
            
            # Create student object
            student_data = {
                "id": student[0],
                "name": student[1],
                "email": student_email,
                "age": student_age,
                "course": student_course
            }
            result.append(student_data)
        
        return jsonify(result), 200
        
    except Exception as error:
        error_response = {"error": str(error)}
        return jsonify(error_response), 500


# READ - Get single student by ID
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Get database connection
    connection = get_db_connection()
    if not connection:
        error_response = {"error": "Database connection failed"}
        return jsonify(error_response), 500
    
    try:
        cursor = connection.cursor()
        
        # Select student by ID
        select_query = "SELECT * FROM student WHERE id = %s"
        cursor.execute(select_query, (student_id,))
        student = cursor.fetchone()
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        # Check if student exists
        if student:
            # Handle empty values
            student_email = student[2]
            if not student_email:
                student_email = ''
                
            student_age = student[3]
            if not student_age:
                student_age = ''
                
            student_course = student[4]
            if not student_course:
                student_course = ''
            
            # Format date
            created_at = student[5].strftime("%Y-%m-%d %H:%M:%S")
            
            # Create response
            response = {
                "id": student[0],
                "name": student[1],
                "email": student_email,
                "age": student_age,
                "course": student_course
            }
            return jsonify(response), 200
        else:
            error_response = {"error": "Student not found"}
            return jsonify(error_response), 404
            
    except Exception as error:
        error_response = {"error": str(error)}
        return jsonify(error_response), 500


# UPDATE - Update student information
@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    # Get data from request
    data = request.get_json()
    
    # Check if name is provided
    if not data:
        error_response = {"error": "No data provided"}
        return jsonify(error_response), 400
    
    if 'name' not in data:
        error_response = {"error": "Name is required"}
        return jsonify(error_response), 400
    
    student_name = data['name'].strip()
    if not student_name:
        error_response = {"error": "Name cannot be empty"}
        return jsonify(error_response), 400
    
    # Get database connection
    connection = get_db_connection()
    if not connection:
        error_response = {"error": "Database connection failed"}
        return jsonify(error_response), 500
    
    try:
        cursor = connection.cursor()
        
        # Prepare student data
        student_email = data.get('email', '').strip()
        if not student_email:
            student_email = None
            
        student_age = data.get('age')
        if not student_age:
            student_age = None
            
        student_course = data.get('course', '').strip()
        if not student_course:
            student_course = None
        
        # Update query
        update_query = "UPDATE student SET name = %s, email = %s, age = %s, course = %s WHERE id = %s"
        values = (student_name, student_email, student_age, student_course, student_id)
        
        # Execute update
        cursor.execute(update_query, values)
        connection.commit()
        
        # Check if student was found and updated
        rows_affected = cursor.rowcount
        if rows_affected == 0:
            cursor.close()
            connection.close()
            error_response = {"error": "Student not found"}
            return jsonify(error_response), 404
        
        # Fetch the updated student
        select_query = "SELECT * FROM student WHERE id = %s"
        cursor.execute(select_query, (student_id,))
        student = cursor.fetchone()
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        # Handle empty values
        student_email = student[2]
        if not student_email:
            student_email = ''
            
        student_age = student[3]
        if not student_age:
            student_age = ''
            
        student_course = student[4]
        if not student_course:
            student_course = ''
        
        # Format date
        created_at = student[5].strftime("%Y-%m-%d %H:%M:%S")
        
        # Prepare response
        response = {
            "id": student[0],
            "name": student[1],
            "email": student_email,
            "age": student_age,
            "course": student_course
        }
        
        return jsonify(response), 200
        
    except Exception as error:
        error_response = {"error": str(error)}
        return jsonify(error_response), 500


# DELETE - Remove student from database
@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    # Get database connection
    connection = get_db_connection()
    if not connection:
        error_response = {"error": "Database connection failed"}
        return jsonify(error_response), 500
    
    try:
        cursor = connection.cursor()
        
        # Delete query
        delete_query = "DELETE FROM student WHERE id = %s"
        cursor.execute(delete_query, (student_id,))
        connection.commit()
        
        # Check if student was found and deleted
        rows_affected = cursor.rowcount
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
        if rows_affected == 0:
            error_response = {"error": "Student not found"}
            return jsonify(error_response), 404
        
        success_response = {"message": "Student deleted successfully"}
        return jsonify(success_response), 200
        
    except Exception as error:
        error_response = {"error": str(error)}
        return jsonify(error_response), 500


# Run the application
if __name__ == '__main__':
    init_db()  # Setup database when app starts
    app.run(debug=True)  # Run with debug mode on
    init_db()
    app.run(debug=True)