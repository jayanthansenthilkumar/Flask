# STUDENT MANAGEMENT SYSTEM - MAIN APPLICATION
# This Flask app manages a database of students with CRUD operations

# ==================== IMPORTS ====================
from flask import Flask, render_template, request, jsonify
import mysql.connector

# ==================== FLASK APP SETUP ====================
# Create the Flask application
app = Flask(__name__)

# ==================== DATABASE CONFIGURATION ====================
# Settings for connecting to MySQL database
DB_HOST = 'localhost'          # Database server address
DB_USER = 'root'               # Database username
DB_PASSWORD = ''               # Database password (CHANGE THIS!)
DB_NAME = 'pycrud'             # Name of database


# ==================== DATABASE CONNECTION FUNCTION ====================
def get_db_connection():
    """
    Creates and returns a connection to the MySQL database.
    Returns: Connection object if successful, None if failed
    """
    try:
        # Try to connect to the MySQL database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Exception as error:
        # If connection fails, print error message
        print("Error connecting to database: " + str(error))
        return None


# ==================== DATABASE INITIALIZATION ====================
def init_db():
    """
    Creates the database and student table if they don't exist.
    This is called when the application starts.
    """
    try:
        # Connect to MySQL without specifying a database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        create_db_query = "CREATE DATABASE IF NOT EXISTS " + DB_NAME
        cursor.execute(create_db_query)
        
        # Select the database to use
        cursor.execute("USE " + DB_NAME)
        
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
        
        # Save all changes
        connection.commit()
        cursor.close()
        connection.close()
        print("Database initialized successfully!")
        
    except Exception as error:
        print("Error initializing database: " + str(error))


# ==================== ROUTES / PAGES ====================

@app.route('/')
def home():
    """Route for the main dashboard page"""
    return render_template('index.html')


@app.route('/students')
def students():
    """Route for the students management page"""
    return render_template('students.html')


# ==================== API ROUTES ====================

@app.route('/api/health')
def health():
    """Health check - returns OK if server is running"""
    return jsonify({"status": "ok"}), 200


# ==================== CREATE - Add New Student ====================
@app.route('/api/students', methods=['POST'])
def create_student():
    """
    Creates a new student in the database.
    Expects JSON data with: name, email, age, course
    """
    # Get JSON data from request
    data = request.get_json()
    
    # Validate that data was sent
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Validate that name is provided (required field)
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    # Get and clean the name
    name = data['name'].strip()
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400
    
    # Get database connection
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        # Get and clean other fields (optional)
        email = data.get('email', '').strip()
        if not email:
            email = None
        
        age = data.get('age')
        if not age:
            age = None
        else:
            age = int(age)
        
        course = data.get('course', '').strip()
        if not course:
            course = None
        
        # Insert new student into database
        insert_query = "INSERT INTO student (name, email, age, course) VALUES (%s, %s, %s, %s)"
        values = (name, email, age, course)
        cursor.execute(insert_query, values)
        connection.commit()
        
        # Get the ID of the newly created student
        new_id = cursor.lastrowid
        
        # Fetch the new student to return it
        cursor.execute("SELECT * FROM student WHERE id = %s", (new_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        # Return the new student as JSON
        response = {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "age": student[3],
            "course": student[4]
        }
        
        return jsonify(response), 201
        
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500


# ==================== READ - Get All Students ====================
@app.route('/api/students', methods=['GET'])
def get_students():
    """
    Retrieves all students from the database.
    Returns a list of all students.
    """
    # Get database connection
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        # Get all students from database
        cursor.execute("SELECT * FROM student ORDER BY id ASC")
        students_list = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        # Convert each student row to a dictionary
        result = []
        for student in students_list:
            student_data = {
                "id": student[0],
                "name": student[1],
                "email": student[2] if student[2] else '',
                "age": student[3] if student[3] else '',
                "course": student[4] if student[4] else ''
            }
            result.append(student_data)
        
        # Return list of students as JSON
        return jsonify(result), 200
        
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500


# ==================== READ - Get Single Student ====================
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Gets a single student by ID from the database.
    Returns the student data if found.
    """
    # Get database connection
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        # Get student by ID
        cursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        # Check if student was found
        if student:
            # Return student as JSON
            response = {
                "id": student[0],
                "name": student[1],
                "email": student[2] if student[2] else '',
                "age": student[3] if student[3] else '',
                "course": student[4] if student[4] else ''
            }
            return jsonify(response), 200
        else:
            # Student not found
            return jsonify({"error": "Student not found"}), 404
            
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500


# ==================== UPDATE - Modify Existing Student ====================
@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Updates an existing student's information.
    Expects JSON data with: name, email, age, course
    """
    # Get JSON data from request
    data = request.get_json()
    
    # Validate that data was sent
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Validate that name is provided
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    # Get and clean the name
    name = data['name'].strip()
    if not name:
        return jsonify({"error": "Name cannot be empty"}), 400
    
    # Get database connection
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        # Get and clean other fields
        email = data.get('email', '').strip()
        if not email:
            email = None
        
        age = data.get('age')
        if not age:
            age = None
        else:
            age = int(age)
        
        course = data.get('course', '').strip()
        if not course:
            course = None
        
        # Update the student in database
        update_query = "UPDATE student SET name = %s, email = %s, age = %s, course = %s WHERE id = %s"
        values = (name, email, age, course, student_id)
        cursor.execute(update_query, values)
        connection.commit()
        
        # Check if student was found and updated
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404
        
        # Fetch the updated student
        cursor.execute("SELECT * FROM student WHERE id = %s", (student_id,))
        student = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        # Return updated student as JSON
        response = {
            "id": student[0],
            "name": student[1],
            "email": student[2] if student[2] else '',
            "age": student[3] if student[3] else '',
            "course": student[4] if student[4] else ''
        }
        
        return jsonify(response), 200
        
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500


# ==================== DELETE - Remove Student ====================
@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Deletes a student from the database.
    Returns success message if deleted.
    """
    # Get database connection
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = connection.cursor()
        
        # Delete the student from database
        delete_query = "DELETE FROM student WHERE id = %s"
        cursor.execute(delete_query, (student_id,))
        connection.commit()
        
        # Check if student was found and deleted
        if cursor.rowcount == 0:
            cursor.close()
            connection.close()
            return jsonify({"error": "Student not found"}), 404
        
        cursor.close()
        connection.close()
        
        # Return success message
        return jsonify({"message": "Student deleted successfully"}), 200
        
    except Exception as error:
        cursor.close()
        connection.close()
        return jsonify({"error": str(error)}), 500


# ==================== MAIN EXECUTION ====================
# ==================== MAIN EXECUTION ====================
if __name__ == '__main__':
    # Initialize database when app starts
    init_db()
    
    # Start the Flask application
    # debug=True means the server will restart on code changes
    app.run(debug=True)