import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'pycrud'

try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()
    
    # Check existing users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    print("Existing users:")
    for user in users:
        print(f"  ID: {user[0]}, Username: {user[1]}, Role: {user[3]}")
    
    print("\nAdding default users if they don't exist...")
    
    # Insert default users
    default_users = [
        ('admin', 'admin123', 'admin'),
        ('student', 'student123', 'student')
    ]
    
    added_count = 0
    for username, password, role in default_users:
        try:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                (username, password, role)
            )
            print(f"  ✓ Added user: {username} (role: {role})")
            added_count += 1
        except mysql.connector.IntegrityError:
            print(f"  - User {username} already exists")
    
    if added_count > 0:
        connection.commit()
        print(f"\n✅ {added_count} default users created successfully!")
    else:
        print("\n✅ All default users already exist!")
    
    cursor.close()
    connection.close()
    
except Exception as error:
    print(f"Error: {str(error)}")
