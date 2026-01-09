import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pycrud'
)
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE colleges ADD COLUMN type VARCHAR(50) DEFAULT 'Private'")
    conn.commit()
    print('✓ Added type column to colleges table')
except Exception as e:
    print(f'Error: {e}')
finally:
    conn.close()
