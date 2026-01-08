# QUICK START GUIDE - PYCRUD

## 🚀 Start the Application (3 steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Flask Server
```bash
python app.py
```

### Step 3: Open in Browser
- **Dashboard**: http://localhost:5000/
- **Students**: http://localhost:5000/students

---

## 📋 File Organization

| File | Purpose | Responsibility |
|------|---------|-----------------|
| `app.py` | Backend Server | Database & APIs |
| `style.css` | Website Styling | How it looks |
| `script.js` | Website Behavior | How it works |
| `index.html` | Dashboard Page | Home page HTML |
| `students.html` | Students Page | Management page HTML |

---

## 🔍 Where is Everything?

### **Add a Student?**
- UI: `students.html` (modal form)
- Logic: `script.js` (createStudent function)
- Database: `app.py` (POST /api/students)

### **View Students?**
- UI: `students.html` (table)
- Logic: `script.js` (loadStudents, displayStudents)
- Database: `app.py` (GET /api/students)

### **Change Colors?**
- File: `style.css`
- Find: `.btn-primary { background: #3b82f6; }`
- Change the color code

### **Change Text?**
- Files: `index.html` or `students.html`
- Find the text and change it directly

### **Add New Functionality?**
1. Add API in `app.py`
2. Add JavaScript function in `script.js`
3. Add HTML button/form in `.html` file
4. Add CSS styling in `style.css`

---

## 🎯 Main Functions to Know

### **JavaScript (script.js)**
```javascript
// Load all students
loadStudents()

// Display students in table
displayStudents(students)

// Create new student
createStudent(studentData)

// Edit student
editStudent(id)

// Update student
updateStudent(id, studentData)

// Delete student
deleteStudent(id)

// Search students
filterStudents(searchTerm)

// Show messages
showError(message)
showSuccess(message)
```

### **Python (app.py)**
```python
# Get database connection
get_db_connection()

# Initialize database
init_db()

# API endpoints
@app.route('/api/students', methods=['POST'])    # Create
@app.route('/api/students', methods=['GET'])     # Read All
@app.route('/api/students/<id>', methods=['GET']) # Read One
@app.route('/api/students/<id>', methods=['PUT']) # Update
@app.route('/api/students/<id>', methods=['DELETE']) # Delete
```

---

## 🎨 Key CSS Classes

```css
/* Main containers */
.sidebar           /* Left menu */
.main-content      /* Page content area */
.header            /* Top bar */

/* Cards and layouts */
.card              /* White boxes */
.card-header       /* Title of card */
.card-body         /* Content of card */

/* Statistics */
.stats-grid        /* Stats container */
.stat-card         /* Individual stat */

/* Forms */
.form-group        /* Form input group */
.form-row          /* Form row (2 columns) */

/* Buttons */
.btn               /* Base button */
.btn-primary       /* Blue button */
.btn-edit          /* Green button */
.btn-delete        /* Red button */

/* Tables */
.data-table        /* Student table */
.data-table th     /* Table header */
.data-table td     /* Table cell */

/* Modal/Popup */
.modal             /* Popup container */
.modal.show        /* Visible modal */
```

---

## 📞 Common Tasks

### **Add a New Column (e.g., Phone Number)**

1. **Database (app.py):**
```python
# In init_db() function, modify CREATE TABLE:
"phone VARCHAR(20),"
```

2. **HTML (students.html):**
```html
<!-- Add input in form -->
<input type="tel" id="student-phone" placeholder="Phone...">
```

3. **JavaScript (script.js):**
```javascript
// In form submission:
phone: document.getElementById('student-phone').value,

// In displayStudents():
html = html + '<td>' + student.phone + '</td>';
```

4. **Python (app.py):**
```python
# In all SQL queries:
"INSERT INTO student (name, email, age, course, phone) VALUES (%s, %s, %s, %s, %s)"
# Add phone to values tuple
phone = data.get('phone', '').strip() or None
```

---

## 🎯 Understanding the Flow

### **Adding a Student - Step by Step**

**Step 1**: User fills form and clicks "Add Student"
```html
<!-- In students.html -->
<input type="text" id="student-name" ...>
<button type="submit">Add Student</button>
```

**Step 2**: JavaScript catches the form submission
```javascript
// In script.js
document.getElementById('student-form').addEventListener('submit', function(e) {
    // Get form values
    const name = document.getElementById('student-name').value;
    // Create student object
    createStudent({ name: name, ... });
});
```

**Step 3**: JavaScript sends data to Flask
```javascript
// In script.js - createStudent()
fetch('/api/students', {
    method: 'POST',
    body: JSON.stringify(studentData)
})
```

**Step 4**: Flask receives request and saves to database
```python
# In app.py - create_student()
@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.get_json()  # Get data from frontend
    # Insert into MySQL
    cursor.execute("INSERT INTO student ... VALUES ...")
```

**Step 5**: Flask returns new student to JavaScript
```python
# app.py returns JSON response
return jsonify(response), 201
```

**Step 6**: JavaScript updates the page
```javascript
# script.js shows success message and reloads students
showSuccess('Student created successfully!')
loadStudents()
```

---

## 🔐 Security Notes

- **Never expose database password** in frontend code
- **Always validate** user input in backend (app.py)
- **Use parameterized queries** (already done: %s placeholders)
- **Escape HTML** (escapeHtml function in script.js)
- **Validate emails** before saving to database

---

## 📊 Database Structure

### **Student Table**
```
id       | name    | email            | age | course
---------|---------|------------------|-----|--------
1        | John    | john@email.com   | 20  | Python
2        | Sarah   | sarah@email.com  | 19  | Java
3        | Mike    | NULL             | 21  | Python
```

### **Field Types**
- `id` - Auto-incrementing integer (primary key)
- `name` - Text (required)
- `email` - Text (optional)
- `age` - Number (optional)
- `course` - Text (optional)

---

## ⚙️ Configuration

### **Change Database Settings (app.py)**
```python
DB_HOST = 'localhost'      # Server address
DB_USER = 'root'           # Username
DB_PASSWORD = ''           # YOUR PASSWORD HERE!
DB_NAME = 'pycrud'         # Database name
```

### **Change Port (app.py)**
```python
# At the bottom:
app.run(debug=True, host='localhost', port=5000)
```

---

## 🐛 Debugging Tips

### **See JavaScript Errors**
1. Press `F12` in browser
2. Click "Console" tab
3. Look for red error messages

### **See Python Errors**
1. Look at the terminal where you ran `python app.py`
2. Red text shows errors
3. Read the error message carefully

### **Check Network Requests**
1. Press `F12` in browser
2. Click "Network" tab
3. Perform an action
4. See requests and responses

### **Test APIs Directly**
Use a tool like Postman or curl:
```bash
# Get all students
curl http://localhost:5000/api/students

# Add a student
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"John","age":20}'
```

---

## 📚 Folder Structure Explained

```
Pycrud/
├── app.py                 ← Main application
├── requirements.txt       ← Dependencies list
├── README.md             ← Full documentation (this is not it)
├── QUICKSTART.md         ← Quick guide (you are here)
│
├── static/               ← Folder for CSS, JS, images
│   ├── style.css        ← All styling
│   └── script.js        ← All JavaScript
│
└── templates/           ← Folder for HTML pages
    ├── index.html       ← Dashboard
    └── students.html    ← Students management
```

---

## ✅ Checklist Before Running

- [ ] Python installed
- [ ] MySQL installed and running
- [ ] MySQL password set in app.py
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] All files present (app.py, style.css, script.js, etc.)
- [ ] No typos in file names

---

## 💡 Tips for Beginners

1. **Read the comments** in code - they explain what's happening
2. **Change one thing at a time** - it's easier to debug
3. **Use browser console (F12)** - it's your friend
4. **Check error messages** - they tell you exactly what's wrong
5. **Start with small modifications** - don't try to change everything at once

---

**That's it! You're ready to code! 🚀**
