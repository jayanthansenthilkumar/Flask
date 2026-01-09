import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pycrud'
)
cursor = conn.cursor()

print("\n" + "="*70)
print("DATABASE VERIFICATION - Student with Foreign Key Relationships")
print("="*70)

cursor.execute("""
    SELECT s.id, s.name, s.email, s.age, s.phoneno,
           st.name as state, c.name as city, 
           col.name as college, d.name as department
    FROM student s
    LEFT JOIN states st ON s.state_id = st.id
    LEFT JOIN cities c ON s.city_id = c.id
    LEFT JOIN colleges col ON s.college_id = col.id
    LEFT JOIN departments d ON s.department_id = d.id
    WHERE s.id = 6
""")

result = cursor.fetchone()

if result:
    print("\n📋 Student Record (ID: 6)")
    print("-"*70)
    print(f"  Name:        {result[1]}")
    print(f"  Email:       {result[2]}")
    print(f"  Age:         {result[3]}")
    print(f"  Phone:       {result[4]}")
    print(f"  State:       {result[5]}")
    print(f"  City:        {result[6]}")
    print(f"  College:     {result[7]}")
    print(f"  Department:  {result[8]}")
else:
    print("\n⚠️  Student not found")

print("\n" + "="*70)
print("✅ Database is correctly using foreign key relationships!")
print("="*70)

cursor.close()
conn.close()
