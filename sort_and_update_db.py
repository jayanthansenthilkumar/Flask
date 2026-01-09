"""
Script to sort colleges in ascending order and update the database
"""
from data import COLLEGES, STATES, CITIES_BY_STATE, DEPARTMENTS, DEPARTMENT_SHORT_NAMES
import mysql.connector

# Sort colleges by name
sorted_colleges = sorted(COLLEGES, key=lambda x: x['name'])

print(f"Total colleges: {len(sorted_colleges)}")
print(f"First college: {sorted_colleges[0]['name']}")
print(f"Last college: {sorted_colleges[-1]['name']}")

# Write sorted colleges back to data.py
with open('data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the COLLEGES section and replace it
import_start = content.find('COLLEGES = [')
import_end = content.find(']', import_start) + 1

# Build the new COLLEGES list
new_colleges_str = 'COLLEGES = [\n'
for college in sorted_colleges:
    new_colleges_str += f'    {{"name": "{college["name"]}", "state": "{college["state"]}", "city": "{college["city"]}", "type": "{college["type"]}"}},\n'
new_colleges_str += ']'

# Replace in content
new_content = content[:import_start] + new_colleges_str + content[import_end:]

# Write back
with open('data.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n✓ Colleges sorted in ascending order in data.py")

# Now update the database
print("\n🔄 Updating database...")

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'pycrud'
}

try:
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    
    # Clear existing data
    print("Clearing existing data...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE colleges")
    cursor.execute("TRUNCATE TABLE cities")
    cursor.execute("TRUNCATE TABLE states")
    cursor.execute("TRUNCATE TABLE departments")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    # Insert states
    print("\n📍 Inserting states...")
    state_ids = {}
    for state in STATES:
        cursor.execute("INSERT INTO states (name) VALUES (%s)", (state,))
        state_ids[state] = cursor.lastrowid
    print(f"✓ Inserted {len(STATES)} states")
    
    # Insert cities
    print("\n🏙️ Inserting cities...")
    city_ids = {}
    for state, cities in CITIES_BY_STATE.items():
        for city in cities:
            cursor.execute(
                "INSERT INTO cities (name, state_id) VALUES (%s, %s)",
                (city, state_ids[state])
            )
            city_ids[f"{city}_{state}"] = cursor.lastrowid
    print(f"✓ Inserted cities")
    
    # Insert colleges (sorted)
    print("\n🎓 Inserting colleges in ascending order...")
    inserted = 0
    skipped = 0
    for college in sorted_colleges:
        city_key = f"{college['city']}_{college['state']}"
        if city_key in city_ids:
            try:
                cursor.execute(
                    "INSERT INTO colleges (name, state_id, city_id, type) VALUES (%s, %s, %s, %s)",
                    (college['name'], state_ids[college['state']], city_ids[city_key], college['type'])
                )
                inserted += 1
            except mysql.connector.IntegrityError:
                skipped += 1
    print(f"✓ Inserted {inserted} colleges (skipped {skipped} duplicates)")
    
    # Insert departments
    print("\n📚 Inserting departments...")
    for dept in DEPARTMENTS:
        short_name = DEPARTMENT_SHORT_NAMES.get(dept, dept[:10])
        cursor.execute(
            "INSERT INTO departments (name, short_name) VALUES (%s, %s)",
            (dept, short_name)
        )
    print(f"✓ Inserted {len(DEPARTMENTS)} departments")
    
    connection.commit()
    cursor.close()
    connection.close()
    
    print("\n✅ Database updated successfully with sorted data!")
    
except Exception as e:
    print(f"\n❌ Error updating database: {e}")
