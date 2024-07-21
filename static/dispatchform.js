document.getElementById('dispatchForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form from submitting the default way

    // Get form values
    const date = document.getElementById('date').value;
    const dispatchNumber = document.getElementById('dispatchNumber').value;
    const itemDescription = document.getElementById('itemDescription').value;
    const quantity = document.getElementById('quantity').value;

    // Simple form validation
    if (!date || !dispatchNumber || !itemDescription || !quantity) {
        displayMessage('Please fill in all fields.', 'error');
        return;
    }

    // You can handle form data here, e.g., send it to a server
    displayMessage('Form submitted successfully!', 'success');
});

function displayMessage(msg, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = msg;
    messageDiv.className = type; // 'error' or 'success'

    if (type === 'success') {
        messageDiv.style.color = 'green';
    } else {
        messageDiv.style.color = 'red';
    }
}
