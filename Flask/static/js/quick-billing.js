/* ========================================
   Quick Billing JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
    // Check for authentication and session validity
    checkSessionValidity();
    
    // Initialize components
    initCustomerSearch();
    initQuickGarments();
    initBillCalculations();
    initPaymentModes();
    initCreateBill();
    
    // Load saved session data
    loadBillingSession();
    
    // Setup periodic session save
    setInterval(saveBillingSession, 30000); // Save every 30 seconds
    
    // Setup time update
    updateTime();
    setInterval(updateTime, 1000);
    
    // Set default delivery date (7 days from now)
    const deliveryDate = document.getElementById('deliveryDate');
    if (deliveryDate) {
        const defaultDate = new Date();
        defaultDate.setDate(defaultDate.getDate() + 7);
        deliveryDate.value = defaultDate.toISOString().split('T')[0];
    }
    
    // Setup page visibility handler for session management
    document.addEventListener('visibilitychange', function() {
        if (!document.hidden) {
            // Page became visible, check session validity
            checkSessionValidity();
        }
    });
    
    // Setup beforeunload handler to save session
    window.addEventListener('beforeunload', function() {
        saveBillingSession();
    });
});

// Check if user session is still valid
function checkSessionValidity() {
    fetch('/api/dashboard-stats/')
        .then(response => {
            if (response.status === 401 || response.status === 403) {
                // Session expired, redirect to login
                showNotification('Session expired. Please login again.', 'error');
                setTimeout(() => {
                    window.location.href = '/login/?next=' + encodeURIComponent(window.location.pathname);
                }, 2000);
            }
        })
        .catch(error => {
            console.warn('Session check failed:', error);
        });
}

// Simple notification system
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existing = document.querySelector('.quick-notification');
    if (existing) existing.remove();
    
    // Create notification
    const notification = document.createElement('div');
    notification.className = `quick-notification alert alert-${type === 'error' ? 'danger' : type === 'success' ? 'success' : 'info'} alert-dismissible fade show`;
    notification.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Store for bill items
let billItems = [];
let selectedCustomer = null;
let stitchingTypes = [];

// Fetch stitching types on load
fetch('/settings/stitching/')
    .then(response => response.text())
    .then(() => {
        // Default stitching types if can't fetch
        stitchingTypes = [
            { id: 1, name: 'Normal', multiplier: 1.0, extra: 0 },
            { id: 2, name: 'Premium', multiplier: 1.5, extra: 50 },
            { id: 3, name: 'Express', multiplier: 2.0, extra: 100 }
        ];
    });

// ========================================
// Update Time Display
// ========================================

function updateTime() {
    const now = new Date();
    const options = { 
        weekday: 'short', 
        day: '2-digit', 
        month: 'short',
        hour: '2-digit', 
        minute: '2-digit'
    };
    document.getElementById('currentTime').textContent = now.toLocaleString('en-IN', options);
}

// ========================================
// Customer Search
// ========================================

function initCustomerSearch() {
    const searchInput = document.getElementById('customerSearch');
    const searchResults = document.getElementById('customerSearchResults');
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();
        
        if (query.length < 2) {
            searchResults.classList.remove('show');
            return;
        }
        
        searchTimeout = setTimeout(() => {
            fetch(`/api/customer-search/?q=${encodeURIComponent(query)}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.customers && data.customers.length > 0) {
                        searchResults.innerHTML = data.customers.map(c => `
                            <div class="customer-result-item" data-customer-id="${c.id}" data-customer-name="${escapeHtml(c.name)}" data-customer-phone="${escapeHtml(c.phone)}" data-customer-address="${escapeHtml(c.address)}">
                                <strong>${escapeHtml(c.name)}</strong>
                                <br><small class="text-muted">${escapeHtml(c.phone)}</small>
                                ${c.address ? `<br><small class="text-muted">${escapeHtml(c.address)}</small>` : ''}
                            </div>
                        `).join('');
                        
                        // Add click event listeners to customer items
                        searchResults.querySelectorAll('.customer-result-item').forEach(item => {
                            item.addEventListener('click', function() {
                                const id = parseInt(this.dataset.customerId);
                                const name = this.dataset.customerName;
                                const phone = this.dataset.customerPhone;
                                const address = this.dataset.customerAddress || '';
                                selectCustomer(id, name, phone, address);
                            });
                        });
                        
                        searchResults.classList.add('show');
                    } else {
                        searchResults.innerHTML = `
                            <div class="customer-result-item text-muted">
                                <i class="bi bi-person-x me-2"></i>No customers found. 
                                <a href="#" class="text-primary" data-bs-toggle="modal" data-bs-target="#newCustomerModal">Add new customer?</a>
                            </div>
                        `;
                        searchResults.classList.add('show');
                    }
                })
                .catch(error => {
                    console.error('Customer search error:', error);
                    searchResults.innerHTML = `
                        <div class="customer-result-item text-danger">
                            Error searching customers. Please try again.
                        </div>
                    `;
                    searchResults.classList.add('show');
                });
        }, 300);
    });
    
    // Hide results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.remove('show');
        }
    });
    
    // Change customer button
    const changeBtn = document.getElementById('changeCustomerBtn');
    if (changeBtn) {
        changeBtn.addEventListener('click', function() {
            clearCustomer();
        });
    }
    
    // Save new customer
    document.getElementById('saveNewCustomer').addEventListener('click', function() {
        const name = document.getElementById('newCustomerName').value.trim();
        const phone = document.getElementById('newCustomerPhone').value.trim();
        const address = document.getElementById('newCustomerAddress').value.trim();
        
        if (!name || !phone) {
            alert('Please enter name and phone number');
            return;
        }
        
        // Set as new customer (will be created on bill save)
        selectedCustomer = { id: null, name, phone, address, isNew: true };
        
        document.getElementById('selectedCustomerName').textContent = name;
        document.getElementById('selectedCustomerDetails').textContent = `${phone}${address ? ' • ' + address : ''}`;
        document.getElementById('selectedCustomerInfo').classList.remove('d-none');
        document.getElementById('customerSearch').value = '';
        
        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('newCustomerModal')).hide();
        
        // Clear form
        document.getElementById('newCustomerName').value = '';
        document.getElementById('newCustomerPhone').value = '';
        document.getElementById('newCustomerAddress').value = '';
        
        updateCreateButton();
    });
}

// Helper function to escape HTML
function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}

// Helper function to escape HTML
function escapeHtml(unsafe) {
    if (!unsafe) return '';
    return String(unsafe)
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}

// Session management functions
function saveBillingSession() {
    const sessionData = {
        selectedCustomer: selectedCustomer,
        billItems: billItems,
        timestamp: new Date().getTime()
    };
    try {
        sessionStorage.setItem('quickBillingSession', JSON.stringify(sessionData));
    } catch (e) {
        console.warn('Could not save billing session:', e);
    }
}

function loadBillingSession() {
    try {
        const sessionData = sessionStorage.getItem('quickBillingSession');
        if (sessionData) {
            const data = JSON.parse(sessionData);
            // Only restore session if less than 30 minutes old
            const now = new Date().getTime();
            const sessionAge = now - (data.timestamp || 0);
            
            if (sessionAge < 30 * 60 * 1000) { // 30 minutes
                if (data.selectedCustomer) {
                    selectedCustomer = data.selectedCustomer;
                    displaySelectedCustomer();
                }
                
                if (data.billItems && data.billItems.length > 0) {
                    billItems = data.billItems;
                    renderBillItems();
                    calculateTotals();
                }
                
                updateCreateButton();
                return true;
            } else {
                // Clear old session
                sessionStorage.removeItem('quickBillingSession');
            }
        }
    } catch (e) {
        console.warn('Could not load billing session:', e);
        sessionStorage.removeItem('quickBillingSession');
    }
    return false;
}

function clearBillingSession() {
    try {
        sessionStorage.removeItem('quickBillingSession');
    } catch (e) {
        console.warn('Could not clear billing session:', e);
    }
}

function displaySelectedCustomer() {
    if (selectedCustomer) {
        document.getElementById('selectedCustomerName').textContent = selectedCustomer.name;
        document.getElementById('selectedCustomerDetails').textContent = `${selectedCustomer.phone}${selectedCustomer.address ? ' • ' + selectedCustomer.address : ''}`;
        document.getElementById('selectedCustomerInfo').classList.remove('d-none');
    }
}

function selectCustomer(id, name, phone, address) {
    selectedCustomer = { id, name, phone, address: address || '' };
    
    displaySelectedCustomer();
    document.getElementById('customerSearch').value = '';
    document.getElementById('customerSearchResults').classList.remove('show');
    
    // Save to session
    saveBillingSession();
    updateCreateButton();
    
    // Show success feedback
    showNotification(`Customer selected: ${name}`, 'success');
}

function clearCustomer() {
    selectedCustomer = null;
    document.getElementById('selectedCustomerInfo').classList.add('d-none');
    document.getElementById('customerSearch').focus();
    document.getElementById('customerSearch').value = '';
    
    // Update session
    saveBillingSession();
    updateCreateButton();
    
    showNotification('Customer selection cleared', 'info');
}

// ========================================
// Quick Garment Buttons
// ========================================

function initQuickGarments() {
    document.querySelectorAll('.quick-garment-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const garmentId = this.dataset.garmentId;
            const garmentName = this.dataset.garmentName;
            const basePrice = parseFloat(this.dataset.basePrice);
            
            // Get selected stitching type
            const stitchingSelect = document.getElementById('stitchingType');
            const stitchingId = stitchingSelect.value;
            const stitchingOption = stitchingSelect.options[stitchingSelect.selectedIndex];
            const stitchingName = stitchingOption.text;
            const multiplier = parseFloat(stitchingOption.dataset.priceMultiplier || 1);
            
            if (!stitchingId) {
                alert('Please select a stitching type first');
                return;
            }
            
            const finalPrice = basePrice * multiplier;
            
            // Add item to bill
            addBillItem({
                garmentId,
                garmentName,
                stitchingId,
                stitchingName,
                quantity: 1,
                price: finalPrice
            });
            
            // Visual feedback
            this.classList.add('active');
            setTimeout(() => this.classList.remove('active'), 200);
        });
    });
}

function addBillItem(item) {
    const itemId = Date.now() + Math.random(); // More unique ID
    const newItem = { ...item, id: itemId };
    billItems.push(newItem);
    
    renderBillItems();
    calculateTotals();
    saveBillingSession();
    updateCreateButton();
    
    showNotification(`Added ${item.garmentName} to bill`, 'success');
}

function removeBillItem(itemId) {
    const itemIndex = billItems.findIndex(item => item.id === itemId);
    if (itemIndex > -1) {
        const removedItem = billItems[itemIndex];
        billItems.splice(itemIndex, 1);
        
        renderBillItems();
        calculateTotals();
        saveBillingSession();
        updateCreateButton();
        
        showNotification(`Removed ${removedItem.garmentName} from bill`, 'info');
    }
}

function updateBillItem(itemId, field, value) {
    const item = billItems.find(i => i.id === itemId);
    if (item) {
        item[field] = value;
        if (field === 'quantity' || field === 'price') {
            calculateTotals();
        }
        saveBillingSession();
    }
}

function renderBillItems() {
    const container = document.getElementById('billItems');
    const itemCountBadge = document.getElementById('billItemCount');
    
    if (billItems.length === 0) {
        container.innerHTML = `
            <div class="text-center text-muted py-4">
                <i class="bi bi-cart display-4 text-muted"></i>
                <p class="mt-2">No items added yet</p>
            </div>
        `;
        itemCountBadge.textContent = '0';
        return;
    }
    
    itemCountBadge.textContent = billItems.length;
    
    container.innerHTML = billItems.map(item => `
        <div class="bill-item" data-id="${item.id}">
            <div>
                <strong>${item.garmentName}</strong>
                <br>
                <select class="form-select form-select-sm mt-1" onchange="updateBillItem(${item.id}, 'stitchingName', this.options[this.selectedIndex].text)">
                    <option value="Normal" ${item.stitchingName === 'Normal' ? 'selected' : ''}>Normal</option>
                    <option value="Premium" ${item.stitchingName === 'Premium' ? 'selected' : ''}>Premium (+50)</option>
                    <option value="Express" ${item.stitchingName === 'Express' ? 'selected' : ''}>Express (+100)</option>
                </select>
            </div>
            <div>
                <input type="number" class="form-control form-control-sm" value="${item.quantity}" 
                       min="1" onchange="updateBillItem(${item.id}, 'quantity', parseInt(this.value)); calculateTotals();">
            </div>
            <div>
                <input type="number" class="form-control form-control-sm" value="${item.price}" 
                       step="0.01" onchange="updateBillItem(${item.id}, 'price', parseFloat(this.value)); calculateTotals();">
            </div>
            <div class="text-end">
                <strong>₹${(item.quantity * item.price).toFixed(2)}</strong>
            </div>
            <button type="button" class="btn btn-outline-danger btn-sm" onclick="removeBillItem(${item.id})">
                <i class="bi bi-trash"></i>
            </button>
        </div>
    `).join('');
}

// ========================================
// Bill Calculations
// ========================================

function initBillCalculations() {
    document.getElementById('discountPercent').addEventListener('input', calculateTotals);
    document.getElementById('advancePaid').addEventListener('input', calculateTotals);
}

function calculateTotals() {
    // Subtotal
    const subtotal = billItems.reduce((sum, item) => sum + (item.quantity * item.price), 0);
    
    // Discount (percentage)
    const discountPercent = parseFloat(document.getElementById('discountPercent').value) || 0;
    const discountAmount = (subtotal * discountPercent) / 100;
    const afterDiscount = Math.max(0, subtotal - discountAmount);
    
    // Tax (0% for now, can be made configurable)
    const tax = 0;
    
    // Grand Total
    const grandTotal = afterDiscount + tax;
    
    // Advance Payment
    const advance = parseFloat(document.getElementById('advancePaid').value) || 0;
    const balance = Math.max(0, grandTotal - advance);
    
    // Update displays
    document.getElementById('billSubtotal').textContent = `₹${subtotal.toFixed(2)}`;
    document.getElementById('billDiscount').textContent = `₹${discountAmount.toFixed(2)}`;
    document.getElementById('billTax').textContent = `₹${tax.toFixed(2)}`;
    document.getElementById('billTotal').textContent = `₹${grandTotal.toFixed(2)}`;
}

// ========================================
// Payment Modes
// ========================================

function initPaymentModes() {
    document.querySelectorAll('.payment-mode-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.payment-mode-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            document.getElementById('paymentMode').value = this.dataset.mode;
        });
    });
}

// ========================================
// Create Bill
// ========================================

function initCreateBill() {
    document.getElementById('createBillBtn').addEventListener('click', createBill);
    document.getElementById('clearBillBtn').addEventListener('click', clearBill);
}

function updateCreateButton() {
    const btn = document.getElementById('createBillBtn');
    btn.disabled = !selectedCustomer || billItems.length === 0;
}

async function createBill() {
    if (!selectedCustomer) {
        showNotification('Please select a customer first', 'error');
        return;
    }
    
    if (billItems.length === 0) {
        showNotification('Please add at least one item to the bill', 'error');
        return;
    }
    
    // Check for required fields
    const deliveryDateInput = document.getElementById('deliveryDate');
    if (deliveryDateInput && !deliveryDateInput.value) {
        showNotification('Please select a delivery date', 'error');
        deliveryDateInput.focus();
        return;
    }
    
    const btn = document.getElementById('createBillBtn');
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Creating...';
    
    try {
        const subtotal = billItems.reduce((sum, item) => sum + (item.quantity * item.price), 0);
        const discountPercent = parseFloat(document.getElementById('discountPercent')?.value || 0);
        const discountAmount = (subtotal * discountPercent) / 100;
        const afterDiscount = Math.max(0, subtotal - discountAmount);
        const tax = 0; // No tax for now
        const total = afterDiscount + tax;
        
        const data = {
            customer_id: selectedCustomer.id,
            customer_name: selectedCustomer.name,
            customer_phone: selectedCustomer.phone,
            customer_address: selectedCustomer.address || '',
            delivery_date: deliveryDateInput?.value || null,
            priority: 'NORMAL',
            items: billItems.map(item => ({
                garment_type: item.garmentId,
                stitching_type: item.stitchingId || 1,
                quantity: item.quantity,
                price: item.price,
                notes: ''
            })),
            subtotal: subtotal,
            discount: discountAmount,
            tax: tax,
            total: total,
            advance: parseFloat(document.getElementById('advancePaid')?.value || 0),
            payment_mode: document.querySelector('.payment-mode-btn.active')?.dataset.mode || 'CASH',
            notes: document.getElementById('specialInstructions')?.value || ''
        };
        
        const response = await fetch('/billing/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            if (response.status === 401 || response.status === 403) {
                showNotification('Session expired. Please login again.', 'error');
                setTimeout(() => {
                    window.location.href = '/login/?next=' + encodeURIComponent(window.location.pathname);
                }, 2000);
                return;
            }
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        
        if (result.success) {
            // Clear session as bill is completed
            clearBillingSession();
            
            // Show success message
            showNotification(`Bill created successfully!\\nOrder: ${result.order_number}\\nInvoice: ${result.invoice_number}`, 'success');
            
            // Clear the form after a short delay
            setTimeout(() => {
                clearBill();
            }, 2000);
            
        } else {
            throw new Error(result.error || 'Unknown error occurred');
        }
    } catch (error) {
        console.error('Bill creation error:', error);
        showNotification('Error creating bill: ' + error.message, 'error');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="bi bi-check-lg me-2"></i>Create Bill & Invoice';
        updateCreateButton();
    }
}

function getCSRFToken() {
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : '';
}

// Clear bill function
function clearBill() {
    billItems = [];
    selectedCustomer = null;
    
    // Clear customer selection
    document.getElementById('selectedCustomerInfo').classList.add('d-none');
    document.getElementById('customerSearch').value = '';
    
    // Clear inputs
    const discountInput = document.getElementById('discountPercent');
    const advanceInput = document.getElementById('advancePaid');
    const instructionsInput = document.getElementById('specialInstructions');
    
    if (discountInput) discountInput.value = '';
    if (advanceInput) advanceInput.value = '';
    if (instructionsInput) instructionsInput.value = '';
    
    // Reset payment mode to cash
    document.querySelectorAll('.payment-mode-btn').forEach(b => b.classList.remove('active'));
    const cashBtn = document.querySelector('.payment-mode-btn[data-mode="CASH"]');
    if (cashBtn) cashBtn.classList.add('active');
    
    // Clear session
    clearBillingSession();
    
    // Re-render
    renderBillItems();
    calculateTotals();
    updateCreateButton();
    
    showNotification('Bill cleared successfully', 'info');
}

// Update create button state
function updateCreateButton() {
    const createBtn = document.getElementById('createBillBtn');
    if (createBtn) {
        const canCreate = selectedCustomer && billItems.length > 0;
        createBtn.disabled = !canCreate;
        
        if (!selectedCustomer) {
            createBtn.innerHTML = '<i class="bi bi-person me-2"></i>Select Customer First';
        } else if (billItems.length === 0) {
            createBtn.innerHTML = '<i class="bi bi-cart me-2"></i>Add Items First';
        } else {
            createBtn.innerHTML = '<i class="bi bi-check-lg me-2"></i>Create Bill & Invoice';
        }
    }
}

// Debounce function for search
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
