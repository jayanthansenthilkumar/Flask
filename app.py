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
    states = [
        # States
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Telangana",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal",
        # Union Territories
        "Andaman and Nicobar Islands",
        "Chandigarh",
        "Dadra and Nagar Haveli and Daman and Diu",
        "Delhi",
        "Jammu and Kashmir",
        "Ladakh",
        "Lakshadweep",
        "Puducherry"
    ]

    return jsonify(states), 200

@app.route('/api/cities', methods=['GET'])
def get_cities():
    state = request.args.get('state', '')
    
    cities_by_state = {

    # States
        "Andhra Pradesh": [
    # Major Cities
    "Visakhapatnam",
    "Vijayawada",
    "Guntur",
    "Nellore",
    "Kurnool",
    "Rajahmundry",
    "Tirupati",
    "Kadapa",
    "Anantapur",
    "Eluru",
    "Ongole",
    "Chittoor",
    "Machilipatnam",
    "Tenali",
    "Proddatur",

    # Vizianagaram / Srikakulam Region
    "Vizianagaram",
    "Srikakulam",
    "Amadalavalasa",
    "Palasa",
    "Bobbili",
    "Narasannapeta",
    "Parvathipuram",
    "Ichchapuram",

    # Visakhapatnam District & Agency Areas
    "Anakapalle",
    "Narsipatnam",
    "Pendurthi",
    "Yelamanchili",
    "Chodavaram",

    # East Godavari
    "Kakinada",
    "Amalapuram",
    "Mandapeta",
    "Ramachandrapuram",
    "Peddapuram",
    "Samalkot",
    "Tuni",
    "Razole",

    # West Godavari
    "Bhimavaram",
    "Tadepalligudem",
    "Narasapuram",
    "Tanuku",
    "Palakollu",
    "Nidadavole",
    "Jangareddygudem",

    # Krishna District
    "Gudivada",
    "Jaggaiahpet",
    "Nuzvid",
    "Mylavaram",
    "Avanigadda",
    "Kaikalur",

    # Guntur & Palnadu
    "Mangalagiri",
    "Narasaraopet",
    "Chilakaluripet",
    "Piduguralla",
    "Sattenapalle",
    "Bapatla",
    "Repalle",
    "Ponnur",

    # Prakasam District
    "Chirala",
    "Markapur",
    "Kandukur",
    "Addanki",
    "Giddalur",

    # SPSR Nellore
    "Kavali",
    "Atmakur",
    "Gudur",
    "Venkatagiri",
    "Naidupet",
    "Sullurpeta",

    # Chittoor District
    "Madanapalle",
    "Punganur",
    "Srikalahasti",
    "Nagari",
    "Palamaner",
    "Vayalpadu",

    # Kadapa (YSR)
    "Pulivendula",
    "Jammalamadugu",
    "Mydukur",
    "Rayachoti",
    "Badvel",
    "Proddatur",

    # Anantapur Region
    "Hindupur",
    "Dharmavaram",
    "Kadiri",
    "Guntakal",
    "Tadipatri",
    "Penukonda",
    "Kalyandurg",

    # Kurnool Region
    "Adoni",
    "Nandyal",
    "Yemmiganur",
    "Allagadda",
    "Banaganapalle",
    "Dhone",
    "Kodumur"
],
        "Arunachal Pradesh": [
    # Capital Region
    "Itanagar",
    "Naharlagun",
    "Nirjuli",
    "Banderdewa",

    # East & West Siang
    "Pasighat",
    "Aalo",
    "Basar",
    "Likabali",
    "Ruksin",

    # Tawang Region
    "Tawang",
    "Lumla",
    "Zemithang",
    "Jang",

    # Lower Subansiri
    "Ziro",
    "Yachuli",

    # Upper Subansiri
    "Daporijo",

    # Papum Pare
    "Sagalee",
    "Kimin",

    # Lohit
    "Tezu",
    "Wakro",

    # Changlang
    "Changlang",
    "Jairampur",
    "Miao",

    # Tirap
    "Khonsa",

    # Longding
    "Longding",

    # Lower Dibang Valley
    "Roing",

    # Upper Dibang Valley
    "Anini",

    # East Kameng
    "Seppa",

    # West Kameng
    "Bomdila",
    "Dirang",

    # Anjaw
    "Hawai",

    # Kra Daadi
    "Palin",

    # Kurung Kumey
    "Koloriang",

    # Lepa Rada
    "Basar",

    # Pakke Kessang
    "Lemmi"
],
        "Assam": [
    # Major Cities
    "Guwahati",
    "Dibrugarh",
    "Silchar",
    "Jorhat",
    "Tezpur",
    "Nagaon",
    "Tinsukia",
    "Sivasagar",
    "Dhubri",
    "Goalpara",

    # Upper Assam
    "Duliajan",
    "Digboi",
    "Margherita",
    "Nazira",
    "Sonari",
    "Moranhat",
    "Naharkatia",

    # Central Assam
    "Hojai",
    "Lanka",
    "Lumding",
    "Kampur",
    "Bokakhat",
    "Dergaon",

    # Lower Assam
    "Barpeta",
    "Barpeta Road",
    "Bongaigaon",
    "Abhayapuri",
    "Bijni",
    "Pathsala",
    "Rangia",

    # Western Assam / Border Towns
    "Dhubri",
    "Gauripur",
    "Bilasipara",
    "Sapatgram",

    # Southern Assam (Barak Valley)
    "Karimganj",
    "Hailakandi",
    "Badarpur",
    "Lala",

    # Northern Bank (North of Brahmaputra)
    "Mangaldoi",
    "Udalguri",
    "Tangla",
    "Dhekiajuli",
    "Biswanath Chariali",

    # Hills & Tribal Areas
    "Diphu",
    "Bokajan",
    "Haflong",
    "Umrangso",

    # Other Important Towns
    "Golaghat",
    "Majuli",
    "Sarupathar",
    "Amguri",
    "Chapar",
    "Lakhipur"
]

        "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga"],
        "Chhattisgarh": ["Raipur", "Bilaspur", "Durg", "Bhilai", "Korba"],
        "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar"],
        "Haryana": ["Gurugram", "Faridabad", "Rohtak", "Panipat", "Ambala"],
        "Himachal Pradesh": ["Shimla", "Solan", "Dharamshala", "Mandi", "Kullu"],
        "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Hazaribagh"],
        "Karnataka": ["Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum"],
        "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kollam"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Thane"],
        "Manipur": ["Imphal", "Thoubal", "Bishnupur"],
        "Meghalaya": ["Shillong", "Tura", "Nongpoh"],
        "Mizoram": ["Aizawl", "Lunglei", "Champhai"],
        "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
        "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur", "Puri"],
        "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer"],
        "Sikkim": ["Gangtok", "Namchi", "Gyalshing"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"],
        "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar"],
        "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Noida", "Ghaziabad"],
        "Uttarakhand": ["Dehradun", "Haridwar", "Rishikesh", "Nainital", "Haldwani"],
        "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Siliguri", "Asansol"],

        # Union Territories
        "Andaman and Nicobar Islands": ["Port Blair", "Diglipur", "Mayabunder"],
        "Chandigarh": ["Chandigarh"],
        "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu", "Silvassa"],
        "Delhi": ["New Delhi", "North Delhi", "South Delhi", "East Delhi", "West Delhi"],
        "Jammu and Kashmir": ["Srinagar", "Jammu", "Anantnag", "Baramulla"],
        "Ladakh": ["Leh", "Kargil"],
        "Lakshadweep": ["Kavaratti", "Agatti", "Minicoy"],
        "Puducherry": ["Puducherry", "Karaikal", "Mahe", "Yanam"]
    }

    
    if state and state in cities_by_state:
        return jsonify(cities_by_state[state]), 200
    else:
        all_cities = []
        for city_list in cities_by_state.values():
            all_cities.extend(city_list)
        return jsonify(sorted(set(all_cities))), 200

@app.route('/api/colleges', methods=['GET'])
def get_colleges():
    state = request.args.get('state', '')
    city = request.args.get('city', '')
    
    colleges_data = [
        {"name": "Indian Institute of Technology Delhi", "state": "Delhi", "city": "New Delhi"},
        {"name": "Indian Institute of Technology Bombay", "state": "Maharashtra", "city": "Mumbai"},
        {"name": "Indian Institute of Technology Madras", "state": "Tamil Nadu", "city": "Chennai"},
        {"name": "Indian Institute of Technology Kanpur", "state": "Uttar Pradesh", "city": "Kanpur"},
        {"name": "Indian Institute of Technology Kharagpur", "state": "West Bengal", "city": "Kharagpur"},
        {"name": "Indian Institute of Science Bangalore", "state": "Karnataka", "city": "Bangalore"},
        {"name": "Jawaharlal Nehru University", "state": "Delhi", "city": "New Delhi"},
        {"name": "University of Delhi", "state": "Delhi", "city": "New Delhi"},
        {"name": "Anna University", "state": "Tamil Nadu", "city": "Chennai"},
        {"name": "Jadavpur University", "state": "West Bengal", "city": "Kolkata"},
        {"name": "Banaras Hindu University", "state": "Uttar Pradesh", "city": "Varanasi"},
        {"name": "Aligarh Muslim University", "state": "Uttar Pradesh", "city": "Aligarh"},
        {"name": "National Institute of Technology Trichy", "state": "Tamil Nadu", "city": "Tiruchirappalli"},
        {"name": "National Institute of Technology Warangal", "state": "Telangana", "city": "Warangal"},
        {"name": "Vellore Institute of Technology", "state": "Tamil Nadu", "city": "Vellore"},
        {"name": "Birla Institute of Technology and Science Pilani", "state": "Rajasthan", "city": "Pilani"},
        {"name": "Manipal Academy of Higher Education", "state": "Karnataka", "city": "Manipal"},
        {"name": "University of Hyderabad", "state": "Telangana", "city": "Hyderabad"},
        {"name": "Amity University Noida", "state": "Uttar Pradesh", "city": "Noida"},
        {"name": "SRM Institute of Science and Technology", "state": "Tamil Nadu", "city": "Chennai"},
        {"name": "Savitribai Phule Pune University", "state": "Maharashtra", "city": "Pune"},
        {"name": "Gujarat University", "state": "Gujarat", "city": "Ahmedabad"},
        {"name": "Osmania University", "state": "Telangana", "city": "Hyderabad"},
        {"name": "Calcutta University", "state": "West Bengal", "city": "Kolkata"},
        {"name": "Mumbai University", "state": "Maharashtra", "city": "Mumbai"},
        {"name": "Bangalore University", "state": "Karnataka", "city": "Bangalore"},
        {"name": "Panjab University", "state": "Punjab", "city": "Chandigarh"},
        {"name": "Lucknow University", "state": "Uttar Pradesh", "city": "Lucknow"},
        {"name": "Cochin University of Science and Technology", "state": "Kerala", "city": "Kochi"},
        {"name": "National Institute of Technology Karnataka", "state": "Karnataka", "city": "Surathkal"}
    ]
    
    filtered_colleges = colleges_data
    
    if state:
        filtered_colleges = [c for c in filtered_colleges if c["state"] == state]
    
    if city:
        filtered_colleges = [c for c in filtered_colleges if c["city"] == city]
    
    college_names = [c["name"] for c in filtered_colleges]
    
    return jsonify(college_names), 200

@app.route('/api/departments', methods=['GET'])
def get_departments():
    engineering_departments = [
        # Core / Traditional Engineering
        "Computer Science and Engineering",
        "Information Technology",
        "Electronics and Communication Engineering",
        "Electrical and Electronics Engineering",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Civil Engineering",
        "Chemical Engineering",
        "Biotechnology Engineering",
        "Aerospace Engineering",
        "Automobile Engineering",
        "Industrial Engineering",
        "Production Engineering",
        "Manufacturing Engineering",
        "Metallurgical Engineering",
        "Mining Engineering",
        "Marine Engineering",
        "Naval Architecture",
        "Textile Engineering",
        "Petroleum Engineering",
        "Ceramic Engineering",
        "Agricultural Engineering",
        "Food Technology",
        "Food Processing Engineering",
        "Dairy Technology",
        "Polymer Engineering",
        "Printing Technology",
        "Paper Technology",
        "Rubber Technology",
        "Leather Technology",
        # Computer / IT Specializations
        "Computer Engineering",
        "Software Engineering",
        "Computer Science and Design",
        "Computer Science and Business Systems",
        "Computer Science and Information Security",
        "Computer Science and Networking",
        "Computer Science and Engineering with specialization in AI",
        "Computer Science and Engineering with specialization in Data Science",
        "Computer Science and Engineering (Cyber Security)",
        "Computer Science and Engineering (Artificial Intelligence and Machine Learning)",
        "Computer Science and Engineering (Cloud Computing)",
        "Computer Science and Artificial Intelligence",
        "Computer Science and Data Science",
        "Computer Science and Cyber Security",
        "Computer Science and Machine Learning",
        "Computer Science and Cloud Computing",
        "Computer Science and Blockchain Technology",
        "Computer Science and Internet of Things",
        "Computer Science and Game Development",
        "Information Science and Engineering",
        "Information Systems Engineering",
        "Data Engineering",
        "Big Data Engineering",
        "Cloud Engineering",
        "DevOps Engineering",
        "Full Stack Engineering",
        # Electronics / Electrical Specializations
        "Electronics and Instrumentation Engineering",
        "Electronics and Telecommunication Engineering",
        "Electronics Engineering",
        "Instrumentation Engineering",
        "Control and Instrumentation Engineering",
        "Power Engineering",
        "Power Systems Engineering",
        "Electrical Power Engineering",
        "Embedded Systems Engineering",
        "VLSI Design",
        "Microelectronics Engineering",
        "Nanoelectronics Engineering",
        "Communication Systems Engineering",
        "Signal Processing Engineering",
        # Mechanical / Allied Specializations
        "Mechatronics Engineering",
        "Robotics Engineering",
        "Industrial Automation Engineering",
        "Automotive Design Engineering",
        "Thermal Engineering",
        "Energy Engineering",
        "Renewable Energy Engineering",
        "Manufacturing Systems Engineering",
        "Production and Industrial Engineering",
        "Tool Engineering",
        "Materials Engineering",
        "Nanotechnology Engineering",
        "Biomedical Engineering",
        "Biomechanical Engineering",
        # Civil / Infrastructure Specializations
        "Structural Engineering",
        "Construction Engineering",
        "Construction Technology",
        "Environmental Engineering",
        "Geotechnical Engineering",
        "Transportation Engineering",
        "Water Resources Engineering",
        "Urban Engineering",
        "Smart Infrastructure Engineering",
        "Earthquake Engineering",
        "Coastal Engineering",
        "Harbour Engineering",
        "Remote Sensing and GIS",
        "Surveying Engineering",
        # Emerging / Interdisciplinary Engineering
        "Artificial Intelligence Engineering",
        "Machine Learning Engineering",
        "Data Analytics Engineering",
        "Data Science Engineering",
        "Cyber Security Engineering",
        "Internet of Things Engineering",
        "Blockchain Engineering",
        "Quantum Computing Engineering",
        "Augmented Reality Engineering",
        "Virtual Reality Engineering",
        "Game Technology Engineering",
        "Financial Technology Engineering",
        "Healthcare Engineering",
        "Systems Engineering",
        "Engineering Physics",
        "Engineering Mathematics",
        "Engineering Design",
        "Sustainable Engineering"
    ]

    return jsonify(engineering_departments), 200

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
        
        state = data.get('state', '').strip()
        if not state:
            state = None
        
        city = data.get('city', '').strip()
        if not city:
            city = None
        
        college = data.get('college', '').strip()
        if not college:
            college = None
        
        department = data.get('department', '').strip()
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
        
        state = data.get('state', '').strip()
        if not state:
            state = None
        
        city = data.get('city', '').strip()
        if not city:
            city = None
        
        college = data.get('college', '').strip()
        if not college:
            college = None
        
        department = data.get('department', '').strip()
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