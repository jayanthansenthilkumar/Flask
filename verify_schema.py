import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'pycrud'

connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = connection.cursor()

print("\n" + "="*70)
print("DATABASE SCHEMA SUMMARY")
print("="*70)

tables = ['states', 'cities', 'colleges', 'departments', 'student']

for table in tables:
    cursor.execute(f'DESCRIBE {table}')
    columns = cursor.fetchall()
    
    print(f"\n📋 Table: {table}")
    print("-"*70)
    print(f"{'Column':<25} {'Type':<25} {'Null':<10} {'Key':<10}")
    print("-"*70)
    
    for row in columns:
        col_name = row[0]
        col_type = row[1]
        col_null = row[2]
        col_key = row[3]
        print(f"{col_name:<25} {col_type:<25} {col_null:<10} {col_key:<10}")

print("\n" + "="*70)
cursor.close()
connection.close()
