// STUDENT MANAGEMENT SYSTEM - JavaScript for Dashboard and Students Pages

let isEditing = false;
let editingId = null;
let allStudents = [];

document.addEventListener('DOMContentLoaded', function() {
    setupMenuToggle();
    setupUserDropdown();
    setupModalControls();
    setupFormValidation();
    loadDashboardData();
    loadDropdownData();
});

function setupMenuToggle() {
    const menuToggleButton = document.getElementById('menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuToggleButton && sidebar) {
        menuToggleButton.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }
}

function setupUserDropdown() {
    const userDropdownBtn = document.getElementById('userDropdownBtn');
    const userDropdownMenu = document.getElementById('userDropdownMenu');
    
    if (userDropdownBtn && userDropdownMenu) {
        userDropdownBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            userDropdownMenu.classList.toggle('show');
        });
        
        document.addEventListener('click', function(e) {
            if (userDropdownMenu.classList.contains('show')) {
                userDropdownMenu.classList.remove('show');
            }
        });
    }
}

function setupModalControls() {
    const modal = document.getElementById('studentModal');
    const openBtn = document.getElementById('openModalBtn');
    const closeBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancel-btn');
    
    if (!modal) {
        return;
    }
    
    if (openBtn) {
        openBtn.addEventListener('click', function() {
            modal.classList.add('show');
            resetForm();
        });
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            modal.classList.remove('show');
            resetForm();
        });
    }
    
    if (cancelBtn) {
        cancelBtn.addEventListener('click', function() {
            modal.classList.remove('show');
            resetForm();
        });
    }
    
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.classList.remove('show');
            resetForm();
        }
    });
}

function loadDropdownData() {
    fetch('/api/states')
        .then(function(response) {
            return response.json();
        })
        .then(function(states) {
            const stateSelect = document.getElementById('student-state');
            if (stateSelect) {
                states.forEach(function(state) {
                    const option = document.createElement('option');
                    option.value = state;
                    option.textContent = state;
                    stateSelect.appendChild(option);
                });
                
                stateSelect.addEventListener('change', function() {
                    const selectedState = this.value;
                    const citySelect = document.getElementById('student-city');
                    const collegeSelect = document.getElementById('student-college');
                    
                    if (selectedState) {
                        loadCities(selectedState);
                    } else {
                        if (citySelect) {
                            citySelect.innerHTML = '<option value="">Select City...</option>';
                            citySelect.disabled = true;
                        }
                        if (collegeSelect) {
                            collegeSelect.innerHTML = '<option value="">Select College...</option>';
                            collegeSelect.disabled = true;
                        }
                    }
                });
            }
        })
        .catch(function(error) {
            console.error('Error loading states:', error);
        });
    
    fetch('/api/departments')
        .then(function(response) {
            return response.json();
        })
        .then(function(departments) {
            const departmentSelect = document.getElementById('student-department');
            if (departmentSelect) {
                departments.forEach(function(department) {
                    const option = document.createElement('option');
                    option.value = department;
                    option.textContent = department;
                    departmentSelect.appendChild(option);
                });
            }
        })
        .catch(function(error) {
            console.error('Error loading departments:', error);
        });
    
    const citySelect = document.getElementById('student-city');
    const collegeSelect = document.getElementById('student-college');
    if (citySelect) citySelect.disabled = true;
    if (collegeSelect) collegeSelect.disabled = true;
}

function loadCities(state) {
    const citySelect = document.getElementById('student-city');
    const collegeSelect = document.getElementById('student-college');
    
    if (!citySelect) return;
    
    citySelect.innerHTML = '<option value="">Select City...</option>';
    if (collegeSelect) {
        collegeSelect.innerHTML = '<option value="">Select College...</option>';
        collegeSelect.disabled = true;
    }
    
    if (!state) {
        citySelect.disabled = true;
        return;
    }
    
    citySelect.disabled = true;
    
    fetch('/api/cities?state=' + encodeURIComponent(state))
        .then(function(response) {
            return response.json();
        })
        .then(function(cities) {
            cities.forEach(function(city) {
                const option = document.createElement('option');
                option.value = city;
                option.textContent = city;
                citySelect.appendChild(option);
            });
            
            citySelect.disabled = false;
            
            const existingListener = citySelect.getAttribute('data-listener');
            if (!existingListener) {
                citySelect.setAttribute('data-listener', 'true');
                citySelect.addEventListener('change', function() {
                    const selectedCity = this.value;
                    const stateSelect = document.getElementById('student-state');
                    const selectedState = stateSelect ? stateSelect.value : '';
                    
                    if (selectedCity && selectedState) {
                        loadColleges(selectedState, selectedCity);
                    } else {
                        if (collegeSelect) {
                            collegeSelect.innerHTML = '<option value="">Select College...</option>';
                            collegeSelect.disabled = true;
                        }
                    }
                });
            }
        })
        .catch(function(error) {
            console.error('Error loading cities:', error);
            citySelect.disabled = false;
        });
}

function loadColleges(state, city) {
    const collegeSelect = document.getElementById('student-college');
    if (!collegeSelect) return;
    
    collegeSelect.innerHTML = '<option value="">Loading colleges...</option>';
    collegeSelect.disabled = true;
    
    if (!state || !city) {
        collegeSelect.innerHTML = '<option value="">Select College...</option>';
        return;
    }
    
    let url = '/api/colleges?state=' + encodeURIComponent(state) + '&city=' + encodeURIComponent(city);
    
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(colleges) {
            collegeSelect.innerHTML = '<option value="">Select College...</option>';
            
            if (colleges.length === 0) {
                const option = document.createElement('option');
                option.value = '';
                option.textContent = 'No colleges found in this city';
                option.disabled = true;
                collegeSelect.appendChild(option);
            } else {
                colleges.forEach(function(college) {
                    const option = document.createElement('option');
                    option.value = college;
                    option.textContent = college;
                    collegeSelect.appendChild(option);
                });
            }
            
            collegeSelect.disabled = false;
        })
        .catch(function(error) {
            console.error('Error loading colleges:', error);
            collegeSelect.innerHTML = '<option value="">Error loading colleges</option>';
            collegeSelect.disabled = false;
        });
}

function setupFormValidation() {
    const studentForm = document.getElementById('student-form');
    
    if (!studentForm) {
        return;
    }
    
    studentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const nameInput = document.getElementById('student-name');
        const emailInput = document.getElementById('student-email');
        const ageInput = document.getElementById('student-age');
        const phonenoInput = document.getElementById('student-phoneno');
        const stateInput = document.getElementById('student-state');
        const cityInput = document.getElementById('student-city');
        const collegeInput = document.getElementById('student-college');
        const departmentInput = document.getElementById('student-department');
        
        const name = nameInput.value.trim();
        const email = emailInput.value.trim();
        const age = ageInput.value;
        const phoneno = phonenoInput.value.trim();
        const state = stateInput.value;
        const city = cityInput.value;
        const college = collegeInput.value;
        const department = departmentInput.value;
        
        if (!name) {
            showError('Please enter a student name');
            return;
        }
        
        const studentData = {
            name: name,
            email: email || null,
            age: age ? parseInt(age) : null,
            phoneno: phoneno || null,
            state: state || null,
            city: city || null,
            college: college || null,
            department: department || null
        };
        
        if (isEditing) {
            updateStudent(editingId, studentData);
        } else {
            createStudent(studentData);
        }
    });
}

function loadDashboardData() {
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'block';
    }
    
    fetch('/api/students')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Failed to load students');
            }
            return response.json();
        })
        .then(function(students) {
            updateDashboardStats(students);
            displayRecentStudents(students);
            
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
        })
        .catch(function(error) {
            console.error('Error loading dashboard:', error);
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
            showError('Error loading dashboard data');
        });
}

function updateDashboardStats(students) {
    const totalStudents = students.length;
    
    const colleges = [];
    for (let i = 0; i < students.length; i++) {
        const college = students[i].college;
        if (college && colleges.indexOf(college) === -1) {
            colleges.push(college);
        }
    }
    
    let totalAge = 0;
    let countWithAge = 0;
    for (let i = 0; i < students.length; i++) {
        if (students[i].age) {
            totalAge = totalAge + parseInt(students[i].age);
            countWithAge = countWithAge + 1;
        }
    }
    const avgAge = countWithAge > 0 ? Math.round(totalAge / countWithAge) : 0;
    
    const totalStudentsElement = document.getElementById('total-students');
    const activeStudentsElement = document.getElementById('active-students');
    const totalCollegesElement = document.getElementById('total-colleges');
    const avgAgeElement = document.getElementById('avg-age');
    
    if (totalStudentsElement) totalStudentsElement.textContent = totalStudents;
    if (activeStudentsElement) activeStudentsElement.textContent = totalStudents;
    if (totalCollegesElement) totalCollegesElement.textContent = colleges.length;
    if (avgAgeElement) avgAgeElement.textContent = avgAge;
}

function displayRecentStudents(students) {
    const tbody = document.getElementById('recent-students-body');
    const noStudentsMsg = document.getElementById('no-students');
    
    if (!tbody) {
        return;
    }
    
    if (students.length === 0) {
        tbody.innerHTML = '';
        if (noStudentsMsg) {
            noStudentsMsg.style.display = 'block';
        }
        return;
    }
    
    if (noStudentsMsg) {
        noStudentsMsg.style.display = 'none';
    }
    
    const recentStudents = students.slice(0, 5);
    
    let html = '';
    for (let i = 0; i < recentStudents.length; i++) {
        const student = recentStudents[i];
        html = html + '<tr>';
        html = html + '<td>' + student.id + '</td>';
        html = html + '<td>' + escapeHtml(student.name) + '</td>';
        html = html + '<td>' + escapeHtml(student.email || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.phoneno || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.college || '-') + '</td>';
        html = html + '</tr>';
    }
    
    tbody.innerHTML = html;
}

function loadStudents() {
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'block';
    }
    
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
            
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
        })
        .catch(function(error) {
            console.error('Error loading students:', error);
            if (loadingElement) {
                loadingElement.style.display = 'none';
            }
            showError('Error loading students');
        });
}

function displayStudents(students) {
    const tbody = document.getElementById('students-body');
    const noStudentsMsg = document.getElementById('no-students');
    
    if (!tbody) {
        return;
    }
    
    if (students.length === 0) {
        tbody.innerHTML = '';
        if (noStudentsMsg) {
            noStudentsMsg.style.display = 'block';
        }
        return;
    }
    
    if (noStudentsMsg) {
        noStudentsMsg.style.display = 'none';
    }
    
    let html = '';
    for (let i = 0; i < students.length; i++) {
        const student = students[i];
        html = html + '<tr data-id="' + student.id + '">';
        html = html + '<td>' + student.id + '</td>';
        html = html + '<td>' + escapeHtml(student.name) + '</td>';
        html = html + '<td>' + escapeHtml(student.email || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.phoneno || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.college || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.department || '-') + '</td>';
        html = html + '<td>';
        html = html + '<button class="btn btn-edit" onclick="editStudent(' + student.id + ')">Edit</button>';
        html = html + '<button class="btn btn-delete" onclick="deleteStudent(' + student.id + ')">Delete</button>';
        html = html + '</td>';
        html = html + '</tr>';
    }
    
    tbody.innerHTML = html;
}

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
        const modal = document.getElementById('studentModal');
        if (modal) {
            modal.classList.remove('show');
        }
        
        resetForm();
        loadStudents();
        showSuccess('Student created successfully!');
    })
    .catch(function(error) {
        console.error('Error creating student:', error);
        showError('Error creating student: ' + error.message);
    });
}

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
            
            const formTitle = document.getElementById('form-title');
            const submitBtn = document.getElementById('submit-btn');
            
            if (formTitle) {
                formTitle.innerHTML = '<i class="ri-edit-line"></i> Edit Student';
            }
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="ri-check-line"></i> Update Student';
            }
            
            const idInput = document.getElementById('student-id');
            const nameInput = document.getElementById('student-name');
            const emailInput = document.getElementById('student-email');
            const ageInput = document.getElementById('student-age');
            const phonenoInput = document.getElementById('student-phoneno');
            const stateInput = document.getElementById('student-state');
            const cityInput = document.getElementById('student-city');
            const collegeInput = document.getElementById('student-college');
            const departmentInput = document.getElementById('student-department');
            
            if (idInput) idInput.value = student.id;
            if (nameInput) nameInput.value = student.name;
            if (emailInput) emailInput.value = student.email || '';
            if (ageInput) ageInput.value = student.age || '';
            if (phonenoInput) phonenoInput.value = student.phoneno || '';
            if (stateInput) {
                stateInput.value = student.state || '';
                if (student.state) {
                    loadCities(student.state);
                }
            }
            if (cityInput) cityInput.value = student.city || '';
            if (collegeInput) {
                if (student.state) {
                    loadColleges(student.state, student.city || '');
                }
                setTimeout(function() {
                    collegeInput.value = student.college || '';
                }, 500);
            }
            if (departmentInput) departmentInput.value = student.department || '';
            
            const modal = document.getElementById('studentModal');
            if (modal) {
                modal.classList.add('show');
            }
            
            if (nameInput) {
                nameInput.focus();
            }
        })
        .catch(function(error) {
            console.error('Error fetching student:', error);
            showError('Error fetching student: ' + error.message);
        });
}

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
        const modal = document.getElementById('studentModal');
        if (modal) {
            modal.classList.remove('show');
        }
        
        resetForm();
        loadStudents();
        showSuccess('Student updated successfully!');
    })
    .catch(function(error) {
        console.error('Error updating student:', error);
        showError('Error updating student: ' + error.message);
    });
}

function deleteStudent(id) {
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
        if (result.isConfirmed) {
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
                console.error('Error deleting student:', error);
                showError('Error deleting student: ' + error.message);
            });
        }
    });
}

function filterStudents(searchTerm) {
    if (!searchTerm) {
        displayStudents(allStudents);
        return;
    }
    
    const filtered = [];
    for (let i = 0; i < allStudents.length; i++) {
        const student = allStudents[i];
        
        const name = student.name ? student.name.toLowerCase() : '';
        const email = student.email ? student.email.toLowerCase() : '';
        const phoneno = student.phoneno ? student.phoneno.toLowerCase() : '';
        const college = student.college ? student.college.toLowerCase() : '';
        const department = student.department ? student.department.toLowerCase() : '';
        
        if (name.indexOf(searchTerm) !== -1 || 
            email.indexOf(searchTerm) !== -1 || 
            phoneno.indexOf(searchTerm) !== -1 ||
            college.indexOf(searchTerm) !== -1 ||
            department.indexOf(searchTerm) !== -1) {
            filtered.push(student);
        }
    }
    
    displayStudents(filtered);
}

const searchInput = document.getElementById('search-input');
if (searchInput) {
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();
        filterStudents(searchTerm);
    });
    loadStudents();
}

function resetForm() {
    isEditing = false;
    editingId = null;
    
    const studentForm = document.getElementById('student-form');
    const formTitle = document.getElementById('form-title');
    const submitBtn = document.getElementById('submit-btn');
    
    if (studentForm) {
        studentForm.reset();
    }
    
    if (formTitle) {
        formTitle.innerHTML = '<i class="ri-user-add-line"></i> Add New Student';
    }
    if (submitBtn) {
        submitBtn.innerHTML = '<i class="ri-add-line"></i> Add Student';
    }
    
    const idInput = document.getElementById('student-id');
    const nameInput = document.getElementById('student-name');
    const emailInput = document.getElementById('student-email');
    const ageInput = document.getElementById('student-age');
    const phonenoInput = document.getElementById('student-phoneno');
    const stateInput = document.getElementById('student-state');
    const cityInput = document.getElementById('student-city');
    const collegeInput = document.getElementById('student-college');
    const departmentInput = document.getElementById('student-department');
    
    if (idInput) idInput.value = '';
    if (nameInput) nameInput.value = '';
    if (emailInput) emailInput.value = '';
    if (ageInput) ageInput.value = '';
    if (phonenoInput) phonenoInput.value = '';
    if (stateInput) stateInput.value = '';
    if (cityInput) {
        cityInput.value = '';
        cityInput.innerHTML = '<option value="">Select City...</option>';
    }
    if (collegeInput) {
        collegeInput.value = '';
        collegeInput.innerHTML = '<option value="">Select College...</option>';
    }
    if (departmentInput) departmentInput.value = '';
}

function showError(message) {
    Swal.fire({
        icon: 'error',
        title: 'Error!',
        text: message,
        confirmButtonColor: '#3b82f6',
        timer: 5000
    });
}

function showSuccess(message) {
    Swal.fire({
        icon: 'success',
        title: 'Success!',
        text: message,
        confirmButtonColor: '#3b82f6',
        timer: 3000,
        showConfirmButton: false
    });
}

function escapeHtml(text) {
    if (!text) {
        return '';
    }
    
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
