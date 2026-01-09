import mysql.connector

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

        # Create users table for authentication
        create_users_table = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(20) NOT NULL DEFAULT 'student',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        cursor.execute(create_users_table)
        print("✓ Users table created")

        # Create question_papers table
        create_papers_table = """
            CREATE TABLE IF NOT EXISTS question_papers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                department VARCHAR(100) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                year VARCHAR(20) NOT NULL,
                link VARCHAR(500) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        cursor.execute(create_papers_table)
        print("✓ Question Papers table created")

        connection.commit()
        cursor.close()
        connection.close()
        print("\n✅ All tables initialized successfully!")

    except mysql.connector.Error as err:
        print(f"Error creating tables: {err}")

if __name__ == "__main__":
    create_tables()
