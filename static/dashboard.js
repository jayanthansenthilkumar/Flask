// Dashboard JavaScript

// Global variables
let studentsData = [];

// Menu toggle for mobile
document.getElementById('menu-toggle').addEventListener('click', function() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
});

// Load dashboard data when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadDashboardData();
});

// Function to load dashboard data
function loadDashboardData() {
    showLoading(true);
    
    // Fetch all students
    fetch('/api/students')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Failed to load students');
            }
            return response.json();
        })
        .then(function(students) {
            studentsData = students;
            updateStatistics(students);
            displayRecentStudents(students);
            showLoading(false);
        })
        .catch(function(error) {
            console.error('Error:', error);
            showLoading(false);
        });
}

// Function to update statistics cards
function updateStatistics(students) {
    // Total students
    var totalStudents = students.length;
    document.getElementById('total-students').textContent = totalStudents;
    
    // Active students (all students are active for now)
    document.getElementById('active-students').textContent = totalStudents;
    
    // Total unique courses
    var courses = [];
    for (var i = 0; i < students.length; i++) {
        var course = students[i].course;
        if (course && courses.indexOf(course) === -1) {
            courses.push(course);
        }
    }
    document.getElementById('total-courses').textContent = courses.length;
    
    // Average age
    var totalAge = 0;
    var countWithAge = 0;
    for (var i = 0; i < students.length; i++) {
        if (students[i].age) {
            totalAge = totalAge + parseInt(students[i].age);
            countWithAge = countWithAge + 1;
        }
    }
    var avgAge = countWithAge > 0 ? Math.round(totalAge / countWithAge) : 0;
    document.getElementById('avg-age').textContent = avgAge;
}

// Function to display recent students (last 5)
function displayRecentStudents(students) {
    var tbody = document.getElementById('recent-students-body');
    var noStudents = document.getElementById('no-students');
    
    if (students.length === 0) {
        tbody.innerHTML = '';
        noStudents.style.display = 'block';
        return;
    }
    
    noStudents.style.display = 'none';
    
    // Get last 5 students
    var recentStudents = students.slice(0, 5);
    
    var html = '';
    for (var i = 0; i < recentStudents.length; i++) {
        var student = recentStudents[i];
        html = html + '<tr>';
        html = html + '<td>' + student.id + '</td>';
        html = html + '<td>' + escapeHtml(student.name) + '</td>';
        html = html + '<td>' + escapeHtml(student.email || '-') + '</td>';
        html = html + '<td>' + (student.age || '-') + '</td>';
        html = html + '<td>' + escapeHtml(student.course || '-') + '</td>';
        html = html + '</tr>';
    }
    
    tbody.innerHTML = html;
}

// Function to show/hide loading
function showLoading(show) {
    var loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = show ? 'block' : 'none';
    }
}

// Function to escape HTML to prevent XSS
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
