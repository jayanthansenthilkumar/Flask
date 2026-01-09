import mysql.connector
from data import STATES, CITIES_BY_STATE, COLLEGES, DEPARTMENTS, DEPARTMENT_SHORT_NAMES

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'pycrud'

def create_tables():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        print("🚀 Creating database tables...")

        # Create states table
        create_states_table = """
            CREATE TABLE IF NOT EXISTS states (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        cursor.execute(create_states_table)
        print("✓ States table created")

        # Create cities table
        create_cities_table = """
            CREATE TABLE IF NOT EXISTS cities (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                state_id INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE,
                UNIQUE KEY unique_city_per_state (name, state_id)
            )
        """
        cursor.execute(create_cities_table)
        print("✓ Cities table created")

        # Create colleges table
        create_colleges_table = """
            CREATE TABLE IF NOT EXISTS colleges (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(250) NOT NULL,
                state_id INT NOT NULL,
                city_id INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE,
                FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
                UNIQUE KEY unique_college (name, city_id)
            )
        """
        cursor.execute(create_colleges_table)
        print("✓ Colleges table created")

        # Create departments table
        create_departments_table = """
            CREATE TABLE IF NOT EXISTS departments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(200) NOT NULL UNIQUE,
                short_name VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        cursor.execute(create_departments_table)
        print("✓ Departments table created")

        # Update student table to use foreign keys
        print("\n🔄 Updating student table to use foreign keys...")
        
        # First, check if columns exist and drop them if needed
        check_columns = """
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = %s 
            AND TABLE_NAME = 'student'
            AND COLUMN_NAME IN ('state', 'city', 'college', 'department')
        """
        cursor.execute(check_columns, (DB_NAME,))
        old_columns = [row[0] for row in cursor.fetchall()]

        if old_columns:
            # Drop old columns
            for col in old_columns:
                try:
                    cursor.execute(f"ALTER TABLE student DROP COLUMN {col}")
                    print(f"  - Dropped old column: {col}")
                except mysql.connector.Error as e:
                    print(f"  - Note: {e.msg}")

        # Add new foreign key columns
        alter_student_queries = [
            "ALTER TABLE student ADD COLUMN state_id INT AFTER phoneno",
            "ALTER TABLE student ADD COLUMN city_id INT AFTER state_id",
            "ALTER TABLE student ADD COLUMN college_id INT AFTER city_id",
            "ALTER TABLE student ADD COLUMN department_id INT AFTER college_id",
            "ALTER TABLE student ADD CONSTRAINT fk_student_state FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE SET NULL",
            "ALTER TABLE student ADD CONSTRAINT fk_student_city FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE SET NULL",
            "ALTER TABLE student ADD CONSTRAINT fk_student_college FOREIGN KEY (college_id) REFERENCES colleges(id) ON DELETE SET NULL",
            "ALTER TABLE student ADD CONSTRAINT fk_student_department FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL"
        ]

        for query in alter_student_queries:
            try:
                cursor.execute(query)
                print(f"  ✓ Executed: {query.split('ADD')[1] if 'ADD' in query else query.split('student')[1]}")
            except mysql.connector.Error as e:
                if 'Duplicate' not in e.msg:
                    print(f"  - Note: {e.msg}")

        connection.commit()
        print("\n✅ All tables created successfully!")
        
        cursor.close()
        connection.close()
        
        return True

    except Exception as error:
        print(f"❌ Error creating tables: {str(error)}")
        return False


def populate_tables():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        print("\n🌱 Populating database with initial data...")

        # Insert states
        print("\n📍 Inserting states...")
        state_ids = {}
        for state in STATES:
            try:
                cursor.execute("INSERT INTO states (name) VALUES (%s)", (state,))
                state_ids[state] = cursor.lastrowid
            except mysql.connector.IntegrityError:
                # State already exists, fetch its ID
                cursor.execute("SELECT id FROM states WHERE name = %s", (state,))
                result = cursor.fetchone()
                if result:
                    state_ids[state] = result[0]
        
        connection.commit()
        print(f"  ✓ Inserted {len(state_ids)} states")

        # Insert cities
        print("\n🏙️ Inserting cities...")
        city_count = 0
        city_ids = {}
        for state, cities in CITIES_BY_STATE.items():
            if state in state_ids:
                state_id = state_ids[state]
                for city in cities:
                    try:
                        cursor.execute(
                            "INSERT INTO cities (name, state_id) VALUES (%s, %s)",
                            (city, state_id)
                        )
                        city_ids[(city, state)] = cursor.lastrowid
                        city_count += 1
                    except mysql.connector.IntegrityError:
                        # City already exists, fetch its ID
                        cursor.execute(
                            "SELECT id FROM cities WHERE name = %s AND state_id = %s",
                            (city, state_id)
                        )
                        result = cursor.fetchone()
                        if result:
                            city_ids[(city, state)] = result[0]
        
        connection.commit()
        print(f"  ✓ Inserted {city_count} cities")

        # Insert colleges
        print("\n🎓 Inserting colleges...")
        college_count = 0
        for college in COLLEGES:
            college_name = college['name']
            state = college['state']
            city = college['city']
            
            if state in state_ids and (city, state) in city_ids:
                state_id = state_ids[state]
                city_id = city_ids[(city, state)]
                
                try:
                    cursor.execute(
                        "INSERT INTO colleges (name, state_id, city_id) VALUES (%s, %s, %s)",
                        (college_name, state_id, city_id)
                    )
                    college_count += 1
                except mysql.connector.IntegrityError:
                    pass  # College already exists
        
        connection.commit()
        print(f"  ✓ Inserted {college_count} colleges")

        # Insert departments
        print("\n🏛️ Inserting departments...")
        dept_count = 0
        for dept in DEPARTMENTS:
            short_name = DEPARTMENT_SHORT_NAMES.get(dept, None)
            try:
                cursor.execute(
                    "INSERT INTO departments (name, short_name) VALUES (%s, %s)",
                    (dept, short_name)
                )
                dept_count += 1
            except mysql.connector.IntegrityError:
                pass  # Department already exists
        
        connection.commit()
        print(f"  ✓ Inserted {dept_count} departments")

        print("\n✅ Database populated successfully!")
        
        cursor.close()
        connection.close()
        
        return True

    except Exception as error:
        print(f"❌ Error populating tables: {str(error)}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("STUDENT MANAGEMENT SYSTEM - Database Table Creation")
    print("=" * 60)
    
    if create_tables():
        populate_tables()
        print("\n" + "=" * 60)
        print("✨ Database setup complete! You can now run the application.")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("⚠️ Database setup failed. Please check the errors above.")
        print("=" * 60)
