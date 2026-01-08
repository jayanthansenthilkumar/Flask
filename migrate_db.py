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

    print("Starting student table schema migration...")

    alter_queries = [
        # Remove legacy column
        "ALTER TABLE student DROP COLUMN course",

        # Add new columns
        "ALTER TABLE student ADD COLUMN phoneno VARCHAR(15)",
        "ALTER TABLE student ADD COLUMN college VARCHAR(200)",
        "ALTER TABLE student ADD COLUMN department VARCHAR(100)"
    ]

    for query in alter_queries:
        try:
            cursor.execute(query)
            print(f"Executed: {query}")
        except mysql.connector.Error as e:
            print(f"Skipped: {e.msg}")

    connection.commit()
    print("Schema migration completed successfully 🚀")

    cursor.close()
    connection.close()

except Exception as error:
    print("Error during schema migration:", str(error))
