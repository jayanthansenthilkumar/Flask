/* ========================================
   Quick Billing JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize
    initCustomerSearch();
    initQuickGarments();
    initBillCalculations();
    initPaymentModes();
    initCreateBill();
    updateTime();
    setInterval(updateTime, 1000);
    
    // Set default delivery date (7 days from now)
    const deliveryDate = document.getElementById('deliveryDate');
    const defaultDate = new Date();
    defaultDate.setDate(defaultDate.getDate() + 7);
    deliveryDate.value = defaultDate.toISOString().split('T')[0];
});

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
    const searchResults = document.getElementById('searchResults');
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();
        
        if (query.length < 2) {
            searchResults.classList.remove('show');
            return;
        }
        
        searchTimeout = setTimeout(() => {
            fetch(`/customers/search/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.customers.length > 0) {
                        searchResults.innerHTML = data.customers.map(c => `
                            <div class="customer-result-item" onclick="selectCustomer(${c.id}, '${c.name}', '${c.phone}')">
                                <strong>${c.name}</strong>
                                <br><small class="text-muted">${c.phone}</small>
                            </div>
                        `).join('');
                        searchResults.classList.add('show');
                    } else {
                        searchResults.innerHTML = `
                            <div class="customer-result-item text-muted">
                                No customers found. 
                                <a href="#" data-bs-toggle="modal" data-bs-target="#newCustomerModal">Add new?</a>
                            </div>
                        `;
                        searchResults.classList.add('show');
                    }
                });
        }, 300);
    });
    
    // Hide results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.remove('show');
        }
    });
    
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
        
        document.getElementById('customerName').textContent = name;
        document.getElementById('customerPhone').textContent = phone;
        document.getElementById('selectedCustomer').style.display = 'block';
        searchInput.value = '';
        
        // Close modal
        bootstrap.Modal.getInstance(document.getElementById('newCustomerModal')).hide();
        
        // Clear form
        document.getElementById('newCustomerName').value = '';
        document.getElementById('newCustomerPhone').value = '';
        document.getElementById('newCustomerAddress').value = '';
        
        updateCreateButton();
    });
}

function selectCustomer(id, name, phone, address) {
    selectedCustomer = { id, name, phone, address };
    
    document.getElementById('selectedCustomerName').textContent = name;
    document.getElementById('selectedCustomerDetails').textContent = `${phone}${address ? ' • ' + address : ''}`;
    document.getElementById('selectedCustomerInfo').classList.remove('d-none');
    document.getElementById('customerSearch').value = '';
    document.getElementById('customerSearchResults').classList.remove('show');
    
    updateCreateButton();
}

function clearCustomer() {
    selectedCustomer = null;
    document.getElementById('selectedCustomerInfo').classList.add('d-none');
    document.getElementById('customerSearch').value = '';
    updateCreateButton();
}

// ========================================
// Quick Garment Buttons
// ========================================

function initQuickGarments() {
    document.querySelectorAll('.quick-garment-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const garmentId = this.dataset.id;
            const garmentName = this.dataset.name;
            const basePrice = parseFloat(this.dataset.price);
            
            // Add item to bill
            addBillItem({
                garmentId,
                garmentName,
                stitchingId: 1,
                stitchingName: 'Normal',
                quantity: 1,
                price: basePrice
            });
            
            // Visual feedback
            this.classList.add('active');
            setTimeout(() => this.classList.remove('active'), 200);
        });
    });
}

function addBillItem(item) {
    const itemId = Date.now();
    billItems.push({ ...item, id: itemId });
    renderBillItems();
    calculateTotals();
    updateCreateButton();
}

function removeBillItem(itemId) {
    billItems = billItems.filter(item => item.id !== itemId);
    renderBillItems();
    calculateTotals();
    updateCreateButton();
}

function updateBillItem(itemId, field, value) {
    const item = billItems.find(i => i.id === itemId);
    if (item) {
        item[field] = value;
        if (field === 'quantity' || field === 'price') {
            calculateTotals();
        }
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
    if (!selectedCustomer || billItems.length === 0) {
        alert('Please select a customer and add items');
        return;
    }
    
    const btn = document.getElementById('createBillBtn');
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Creating...';
    
    try {
        const subtotal = billItems.reduce((sum, item) => sum + (item.quantity * item.price), 0);
        const discountPercent = parseFloat(document.getElementById('discountPercent').value) || 0;
        const discountAmount = (subtotal * discountPercent) / 100;
        const afterDiscount = Math.max(0, subtotal - discountAmount);
        const tax = 0; // No tax for now
        const total = afterDiscount + tax;
        
        const data = {
            customer_id: selectedCustomer.id,
            customer_name: selectedCustomer.name,
            customer_phone: selectedCustomer.phone,
            customer_address: selectedCustomer.address || '',
            delivery_date: document.getElementById('deliveryDate').value,
            priority: 'NORMAL', // Default priority
            items: billItems.map(item => ({
                garment_type: item.garmentId,
                stitching_type: item.stitchingId || 1, // Default stitching type
                quantity: item.quantity,
                price: item.price,
                notes: ''
            })),
            subtotal: subtotal,
            discount: discountAmount,
            tax: tax,
            total: total,
            advance: parseFloat(document.getElementById('advancePaid').value) || 0,
            payment_mode: document.querySelector('.payment-mode-btn.active')?.dataset.mode || 'CASH',
            notes: document.getElementById('specialInstructions').value
        };
        
        const response = await fetch('/billing/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.success) {
            // Show success message and redirect
            alert(`Bill created successfully!\nOrder: ${result.order_number}\nInvoice: ${result.invoice_number}`);
            
            // Clear the form
            clearBill();
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error creating bill: ' + error.message);
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
    document.getElementById('discountPercent').value = '';
    document.getElementById('advancePaid').value = '';
    document.getElementById('specialInstructions').value = '';
    
    // Reset payment mode to cash
    document.querySelectorAll('.payment-mode-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('.payment-mode-btn[data-mode="CASH"]').classList.add('active');
    
    // Re-render
    renderBillItems();
    calculateTotals();
    updateCreateButton();
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
