// Students Management JavaScript

// Global variables
let isEditing = false;
let editingId = null;
let allStudents = [];

// Menu toggle for mobile
document.getElementById('menu-toggle').addEventListener('click', function() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
});

// Load students when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadStudents();
});

// Form submission event
document.getElementById('student-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    var name = document.getElementById('student-name').value.trim();
    var email = document.getElementById('student-email').value.trim();
    var age = document.getElementById('student-age').value;
    var course = document.getElementById('student-course').value.trim();
    
    if (!name) {
        return;
    }

    var studentData = {
        name: name,
        email: email || null,
        age: age ? parseInt(age) : null,
        course: course || null
    };

    if (isEditing) {
        updateStudent(editingId, studentData);
    } else {
        createStudent(studentData);
    }
});

// Cancel button event
document.getElementById('cancel-btn').addEventListener('click', function() {
    resetForm();
});

// Search functionality
document.getElementById('search-input').addEventListener('input', function(e) {
    var searchTerm = e.target.value.toLowerCase();
    filterStudents(searchTerm);
});

// Function to load all students
function loadStudents() {
    showLoading(true);
    
    fetch('/api/students')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Failed to load students');
            }
            return response.json();
        })
        .then(function(students) {
            allStudents = students;
            displayStudents(students);
            showLoading(false);
        })
        .catch(function(error) {
            showError('Error loading students: ' + error.message);
            showLoading(false);
        });
}

// Function to display students in table
function displayStudents(students) {
    var tbody = document.getElementById('students-body');
    var noStudents = document.getElementById('no-students');
    
    if (students.length === 0) {
        tbody.innerHTML = '';
        noStudents.style.display = 'block';
        return;
    }

    noStudents.style.display = 'none';
    
    var html = '';
    for (var i = 0; i < students.length; i++) {
        var student = students[i];
        html = html + '<tr data-id="' + student.id + '">';
        html = html + '<td>' + student.id + '</td>';
        html = html + '<td>' + escapeHtml(student.name) + '</td>';
        html = html + '<td>' + escapeHtml(student.email || '-') + '</td>';
        html = html + '<td>' + (student.age || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.course || '-') + '</td>';
        html = html + '<td>';
        html = html + '<button class="btn btn-edit" onclick="editStudent(' + student.id + ')">Edit</button>';
        html = html + '<button class="btn btn-delete" onclick="deleteStudent(' + student.id + ')">Delete</button>';
        html = html + '</td>';
        html = html + '</tr>';
    }
    
    tbody.innerHTML = html;
}

// Function to create new student
function createStudent(studentData) {
    fetch('/api/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
    .then(function(response) {
        if (!response.ok) {
            return response.json().then(function(error) {
                throw new Error(error.error || 'Failed to create student');
            });
        }
        return response.json();
    })
    .then(function(data) {
        resetForm();
        loadStudents();
        showSuccess('Student created successfully!');
    })
    .catch(function(error) {
        showError('Error creating student: ' + error.message);
    });
}

// Function to edit student
function editStudent(id) {
    fetch('/api/students/' + id)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Failed to fetch student');
            }
            return response.json();
        })
        .then(function(student) {
            isEditing = true;
            editingId = id;
            
            document.getElementById('form-title').textContent = 'Edit Student';
            document.getElementById('student-id').value = student.id;
            document.getElementById('student-name').value = student.name;
            document.getElementById('student-email').value = student.email || '';
            document.getElementById('student-age').value = student.age || '';
            document.getElementById('student-course').value = student.course || '';
            document.getElementById('submit-btn').textContent = 'Update Student';
            document.getElementById('cancel-btn').style.display = 'inline-block';
            
            document.getElementById('student-name').focus();
            
            // Scroll to form
            document.querySelector('.card').scrollIntoView({ behavior: 'smooth' });
        })
        .catch(function(error) {
            showError('Error fetching student: ' + error.message);
        });
}

// Function to update student
function updateStudent(id, studentData) {
    fetch('/api/students/' + id, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
    .then(function(response) {
        if (!response.ok) {
            return response.json().then(function(error) {
                throw new Error(error.error || 'Failed to update student');
            });
        }
        return response.json();
    })
    .then(function(data) {
        resetForm();
        loadStudents();
        showSuccess('Student updated successfully!');
    })
    .catch(function(error) {
        showError('Error updating student: ' + error.message);
    });
}

// Function to delete student
function deleteStudent(id) {
    if (!confirm('Are you sure you want to delete this student?')) {
        return;
    }

    fetch('/api/students/' + id, {
        method: 'DELETE'
    })
    .then(function(response) {
        if (!response.ok) {
            return response.json().then(function(error) {
                throw new Error(error.error || 'Failed to delete student');
            });
        }
        return response.json();
    })
    .then(function(data) {
        loadStudents();
        showSuccess('Student deleted successfully!');
    })
    .catch(function(error) {
        showError('Error deleting student: ' + error.message);
    });
}

// Function to reset form
function resetForm() {
    isEditing = false;
    editingId = null;
    
    document.getElementById('form-title').textContent = 'Add New Student';
    document.getElementById('student-id').value = '';
    document.getElementById('student-name').value = '';
    document.getElementById('student-email').value = '';
    document.getElementById('student-age').value = '';
    document.getElementById('student-course').value = '';
    document.getElementById('submit-btn').textContent = 'Add Student';
    document.getElementById('cancel-btn').style.display = 'none';
}

// Function to filter students based on search
function filterStudents(searchTerm) {
    if (!searchTerm) {
        displayStudents(allStudents);
        return;
    }
    
    var filtered = [];
    for (var i = 0; i < allStudents.length; i++) {
        var student = allStudents[i];
        var name = student.name ? student.name.toLowerCase() : '';
        var email = student.email ? student.email.toLowerCase() : '';
        var course = student.course ? student.course.toLowerCase() : '';
        
        if (name.indexOf(searchTerm) !== -1 || 
            email.indexOf(searchTerm) !== -1 || 
            course.indexOf(searchTerm) !== -1) {
            filtered.push(student);
        }
    }
    
    displayStudents(filtered);
}

// Helper function to show loading
function showLoading(show) {
    var loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = show ? 'block' : 'none';
    }
}

// Helper function to show error message
function showError(message) {
    var errorDiv = document.getElementById('error-message');
    if (!errorDiv) {
        return;
    }
    
    errorDiv.textContent = message;
    errorDiv.className = 'alert error';
    errorDiv.style.display = 'block';
    
    setTimeout(function() {
        errorDiv.style.display = 'none';
    }, 5000);
}

// Helper function to show success message
function showSuccess(message) {
    var errorDiv = document.getElementById('error-message');
    if (!errorDiv) {
        return;
    }
    
    errorDiv.textContent = message;
    errorDiv.className = 'alert success';
    errorDiv.style.display = 'block';
    
    setTimeout(function() {
        errorDiv.style.display = 'none';
    }, 3000);
}

// Helper function to escape HTML
function escapeHtml(text) {
    if (!text) {
        return '';
    }
    var map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;'
    };
    return String(text).replace(/[&<>"']/g, function(char) {
        return map[char];
    });
}
