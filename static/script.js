// STUDENT MANAGEMENT SYSTEM - MAIN JAVASCRIPT
// This file handles all functionality for dashboard and students pages

// ==================== GLOBAL VARIABLES ====================
let isEditing = false;          // Track if we're editing a student
let editingId = null;           // Store the ID of student being edited
let allStudents = [];           // Store all students data

// ==================== INITIALIZATION ====================
// Run this code when page loads
document.addEventListener('DOMContentLoaded', function() {
    setupMenuToggle();           // Setup mobile menu toggle
    setupUserDropdown();         // Setup user dropdown menu
    setupModalControls();        // Setup modal if on students page
    setupFormValidation();       // Setup form validation if on students page
    loadDashboardData();         // Load dashboard data
});

// ==================== MOBILE MENU TOGGLE ====================
function setupMenuToggle() {
    // Find menu toggle button
    const menuToggleButton = document.getElementById('menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    // If toggle button exists, add click listener
    if (menuToggleButton && sidebar) {
        menuToggleButton.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }
}

// ==================== USER DROPDOWN MENU ====================
function setupUserDropdown() {
    // Find dropdown elements
    const userDropdownBtn = document.getElementById('userDropdownBtn');
    const userDropdownMenu = document.getElementById('userDropdownMenu');
    
    // If elements exist, add event listeners
    if (userDropdownBtn && userDropdownMenu) {
        // Open dropdown when button is clicked
        userDropdownBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            userDropdownMenu.classList.toggle('show');
        });
        
        // Close dropdown when clicking anywhere else
        document.addEventListener('click', function(e) {
            if (userDropdownMenu.classList.contains('show')) {
                userDropdownMenu.classList.remove('show');
            }
        });
    }
}

// ==================== MODAL CONTROLS (STUDENTS PAGE) ====================
function setupModalControls() {
    // Find modal elements
    const modal = document.getElementById('studentModal');
    const openBtn = document.getElementById('openModalBtn');
    const closeBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancel-btn');
    
    // If modal doesn't exist, we're on dashboard page - exit function
    if (!modal) {
        return;
    }
    
    // Open modal when "Add New Student" button is clicked
    if (openBtn) {
        openBtn.addEventListener('click', function() {
            modal.classList.add('show');
            resetForm();
        });
    }
    
    // Close modal when close button is clicked
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            modal.classList.remove('show');
            resetForm();
        });
    }
    
    // Close modal when cancel button is clicked
    if (cancelBtn) {
        cancelBtn.addEventListener('click', function() {
            modal.classList.remove('show');
            resetForm();
        });
    }
    
    // Close modal when clicking outside the modal
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.remove('show');
            resetForm();
        }
    });
}

// ==================== FORM VALIDATION (STUDENTS PAGE) ====================
function setupFormValidation() {
    // Find student form
    const studentForm = document.getElementById('student-form');
    
    // If form doesn't exist, we're on dashboard page - exit function
    if (!studentForm) {
        return;
    }
    
    // When form is submitted
    studentForm.addEventListener('submit', function(e) {
        // Stop form from submitting normally
        e.preventDefault();
        
        // Get form values
        const nameInput = document.getElementById('student-name');
        const emailInput = document.getElementById('student-email');
        const ageInput = document.getElementById('student-age');
        const courseInput = document.getElementById('student-course');
        
        // Get and clean the values
        const name = nameInput.value.trim();
        const email = emailInput.value.trim();
        const age = ageInput.value;
        const course = courseInput.value.trim();
        
        // Check if name is provided (it's required)
        if (!name) {
            showError('Please enter a student name');
            return;
        }
        
        // Create student object
        const studentData = {
            name: name,
            email: email || null,
            age: age ? parseInt(age) : null,
            course: course || null
        };
        
        // If editing, update student. Otherwise, create new student
        if (isEditing) {
            updateStudent(editingId, studentData);
        } else {
            createStudent(studentData);
        }
    });
}

// ==================== DASHBOARD FUNCTIONS ====================
function loadDashboardData() {
    // Show loading message
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'block';
    }
    
    // Get all students from server
    fetch('/api/students')
        .then(function(response) {
            // If response is not OK, throw error
            if (!response.ok) {
                throw new Error('Failed to load students');
            }
            // Convert response to JSON
            return response.json();
        })
        .then(function(students) {
            // Update stats and recent students
            updateDashboardStats(students);
            displayRecentStudents(students);
            
            // Hide loading message
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
        })
        .catch(function(error) {
            // Show error message
            console.error('Error loading dashboard:', error);
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
            showError('Error loading dashboard data');
        });
}

function updateDashboardStats(students) {
    // Calculate total students
    const totalStudents = students.length;
    
    // Get unique courses
    const courses = [];
    for (let i = 0; i < students.length; i++) {
        const course = students[i].course;
        if (course && courses.indexOf(course) === -1) {
            courses.push(course);
        }
    }
    
    // Calculate average age
    let totalAge = 0;
    let countWithAge = 0;
    for (let i = 0; i < students.length; i++) {
        if (students[i].age) {
            totalAge = totalAge + parseInt(students[i].age);
            countWithAge = countWithAge + 1;
        }
    }
    const avgAge = countWithAge > 0 ? Math.round(totalAge / countWithAge) : 0;
    
    // Update stat cards on page
    const totalStudentsElement = document.getElementById('total-students');
    const activeStudentsElement = document.getElementById('active-students');
    const totalCoursesElement = document.getElementById('total-courses');
    const avgAgeElement = document.getElementById('avg-age');
    
    if (totalStudentsElement) totalStudentsElement.textContent = totalStudents;
    if (activeStudentsElement) activeStudentsElement.textContent = totalStudents;
    if (totalCoursesElement) totalCoursesElement.textContent = courses.length;
    if (avgAgeElement) avgAgeElement.textContent = avgAge;
}

function displayRecentStudents(students) {
    // Find table body element
    const tbody = document.getElementById('recent-students-body');
    const noStudentsMsg = document.getElementById('no-students');
    
    // If elements don't exist, we're on students page - exit function
    if (!tbody) {
        return;
    }
    
    // If no students, show message
    if (students.length === 0) {
        tbody.innerHTML = '';
        if (noStudentsMsg) {
            noStudentsMsg.style.display = 'block';
        }
        return;
    }
    
    // Hide "no students" message
    if (noStudentsMsg) {
        noStudentsMsg.style.display = 'none';
    }
    
    // Get last 5 students (most recent first)
    const recentStudents = students.slice(0, 5);
    
    // Build HTML for each student
    let html = '';
    for (let i = 0; i < recentStudents.length; i++) {
        const student = recentStudents[i];
        html = html + '<tr>';
        html = html + '<td>' + student.id + '</td>';
        html = html + '<td>' + escapeHtml(student.name) + '</td>';
        html = html + '<td>' + escapeHtml(student.email || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.course || '-') + '</td>';
        html = html + '</tr>';
    }
    
    // Put HTML into table
    tbody.innerHTML = html;
}

// ==================== STUDENTS PAGE FUNCTIONS ====================
function loadStudents() {
    // Show loading message
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'block';
    }
    
    // Get all students from server
    fetch('/api/students')
        .then(function(response) {
            // If response is not OK, throw error
            if (!response.ok) {
                throw new Error('Failed to load students');
            }
            // Convert response to JSON
            return response.json();
        })
        .then(function(students) {
            // Store students and display them
            allStudents = students;
            displayStudents(students);
            
            // Hide loading message
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
        })
        .catch(function(error) {
            // Show error message
            console.error('Error loading students:', error);
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
            showError('Error loading students');
        });
}

function displayStudents(students) {
    // Find table body element
    const tbody = document.getElementById('students-body');
    const noStudentsMsg = document.getElementById('no-students');
    
    // If elements don't exist, exit function
    if (!tbody) {
        return;
    }
    
    // If no students, show message
    if (students.length === 0) {
        tbody.innerHTML = '';
        if (noStudentsMsg) {
            noStudentsMsg.style.display = 'block';
        }
        return;
    }
    
    // Hide "no students" message
    if (noStudentsMsg) {
        noStudentsMsg.style.display = 'none';
    }
    
    // Build HTML for each student row
    let html = '';
    for (let i = 0; i < students.length; i++) {
        const student = students[i];
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
    
    // Put HTML into table
    tbody.innerHTML = html;
}

// ==================== CREATE STUDENT ====================
function createStudent(studentData) {
    // Send POST request to create student
    fetch('/api/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
    .then(function(response) {
        // If response is not OK, get error message
        if (!response.ok) {
            return response.json().then(function(error) {
                throw new Error(error.error || 'Failed to create student');
            });
        }
        // Convert response to JSON
        return response.json();
    })
    .then(function(data) {
        // Close modal
        const modal = document.getElementById('studentModal');
        if (modal) {
            modal.classList.remove('show');
        }
        
        // Reset form and reload students
        resetForm();
        loadStudents();
        showSuccess('Student created successfully!');
    })
    .catch(function(error) {
        // Show error message
        console.error('Error creating student:', error);
        showError('Error creating student: ' + error.message);
    });
}

// ==================== READ / FETCH SINGLE STUDENT ====================
function editStudent(id) {
    // Get student data from server
    fetch('/api/students/' + id)
        .then(function(response) {
            // If response is not OK, throw error
            if (!response.ok) {
                throw new Error('Failed to fetch student');
            }
            // Convert response to JSON
            return response.json();
        })
        .then(function(student) {
            // Set edit mode
            isEditing = true;
            editingId = id;
            
            // Update form title and button text
            const formTitle = document.getElementById('form-title');
            const submitBtn = document.getElementById('submit-btn');
            
            if (formTitle) {
                formTitle.innerHTML = '<i class="ri-edit-line"></i> Edit Student';
            }
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="ri-check-line"></i> Update Student';
            }
            
            // Fill form with student data
            const idInput = document.getElementById('student-id');
            const nameInput = document.getElementById('student-name');
            const emailInput = document.getElementById('student-email');
            const ageInput = document.getElementById('student-age');
            const courseInput = document.getElementById('student-course');
            
            if (idInput) idInput.value = student.id;
            if (nameInput) nameInput.value = student.name;
            if (emailInput) emailInput.value = student.email || '';
            if (ageInput) ageInput.value = student.age || '';
            if (courseInput) courseInput.value = student.course || '';
            
            // Open modal
            const modal = document.getElementById('studentModal');
            if (modal) {
                modal.classList.add('show');
            }
            
            // Focus on name field
            if (nameInput) {
                nameInput.focus();
            }
        })
        .catch(function(error) {
            // Show error message
            console.error('Error fetching student:', error);
            showError('Error fetching student: ' + error.message);
        });
}

// ==================== UPDATE STUDENT ====================
function updateStudent(id, studentData) {
    // Send PUT request to update student
    fetch('/api/students/' + id, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
    .then(function(response) {
        // If response is not OK, get error message
        if (!response.ok) {
            return response.json().then(function(error) {
                throw new Error(error.error || 'Failed to update student');
            });
        }
        // Convert response to JSON
        return response.json();
    })
    .then(function(data) {
        // Close modal
        const modal = document.getElementById('studentModal');
        if (modal) {
            modal.classList.remove('show');
        }
        
        // Reset form and reload students
        resetForm();
        loadStudents();
        showSuccess('Student updated successfully!');
    })
    .catch(function(error) {
        // Show error message
        console.error('Error updating student:', error);
        showError('Error updating student: ' + error.message);
    });
}

// ==================== DELETE STUDENT ====================
function deleteStudent(id) {
    // Show confirmation dialog using SweetAlert
    Swal.fire({
        title: 'Are you sure?',
        text: 'Do you want to delete this student? You cannot undo this action.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#ef4444',
        cancelButtonColor: '#64748b',
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'Cancel'
    }).then(function(result) {
        // If user confirmed deletion
        if (result.isConfirmed) {
            // Send DELETE request
            fetch('/api/students/' + id, {
                method: 'DELETE'
            })
            .then(function(response) {
                // If response is not OK, get error message
                if (!response.ok) {
                    return response.json().then(function(error) {
                        throw new Error(error.error || 'Failed to delete student');
                    });
                }
                // Convert response to JSON
                return response.json();
            })
            .then(function(data) {
                // Reload students list
                loadStudents();
                showSuccess('Student deleted successfully!');
            })
            .catch(function(error) {
                // Show error message
                console.error('Error deleting student:', error);
                showError('Error deleting student: ' + error.message);
            });
        }
    });
}

// ==================== SEARCH STUDENTS ====================
function filterStudents(searchTerm) {
    // If search is empty, show all students
    if (!searchTerm) {
        displayStudents(allStudents);
        return;
    }
    
    // Filter students that match search term
    const filtered = [];
    for (let i = 0; i < allStudents.length; i++) {
        const student = allStudents[i];
        
        // Convert search and student data to lowercase
        const name = student.name ? student.name.toLowerCase() : '';
        const email = student.email ? student.email.toLowerCase() : '';
        const course = student.course ? student.course.toLowerCase() : '';
        
        // Check if search term matches any field
        if (name.indexOf(searchTerm) !== -1 || 
            email.indexOf(searchTerm) !== -1 || 
            course.indexOf(searchTerm) !== -1) {
            filtered.push(student);
        }
    }
    
    // Display filtered students
    displayStudents(filtered);
}

// Setup search input if on students page
const searchInput = document.getElementById('search-input');
if (searchInput) {
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();
        filterStudents(searchTerm);
    });
    // Load students when page loads
    loadStudents();
}

// ==================== FORM HELPERS ====================
function resetForm() {
    // Reset edit mode
    isEditing = false;
    editingId = null;
    
    // Find form and reset elements
    const studentForm = document.getElementById('student-form');
    const formTitle = document.getElementById('form-title');
    const submitBtn = document.getElementById('submit-btn');
    
    // Reset form fields
    if (studentForm) {
        studentForm.reset();
    }
    
    // Reset form title and button text
    if (formTitle) {
        formTitle.innerHTML = '<i class="ri-user-add-line"></i> Add New Student';
    }
    if (submitBtn) {
        submitBtn.innerHTML = '<i class="ri-add-line"></i> Add Student';
    }
    
    // Clear input values
    const idInput = document.getElementById('student-id');
    const nameInput = document.getElementById('student-name');
    const emailInput = document.getElementById('student-email');
    const ageInput = document.getElementById('student-age');
    const courseInput = document.getElementById('student-course');
    
    if (idInput) idInput.value = '';
    if (nameInput) nameInput.value = '';
    if (emailInput) emailInput.value = '';
    if (ageInput) ageInput.value = '';
    if (courseInput) courseInput.value = '';
}

// ==================== MESSAGE HELPERS ====================
function showError(message) {
    // Show error message using SweetAlert
    Swal.fire({
        icon: 'error',
        title: 'Error!',
        text: message,
        confirmButtonColor: '#3b82f6',
        timer: 5000
    });
}

function showSuccess(message) {
    // Show success message using SweetAlert
    Swal.fire({
        icon: 'success',
        title: 'Success!',
        text: message,
        confirmButtonColor: '#3b82f6',
        timer: 3000,
        showConfirmButton: false
    });
}

// ==================== SECURITY HELPER ====================
// This function prevents XSS attacks by escaping HTML
function escapeHtml(text) {
    // If text is empty, return empty string
    if (!text) {
        return '';
    }
    
    // Create a temporary div to escape HTML
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
