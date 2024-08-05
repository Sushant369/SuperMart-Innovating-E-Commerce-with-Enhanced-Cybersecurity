document.addEventListener('DOMContentLoaded', function() {
    // Your existing code
    console.log("Welcome to Walmart's website!");
});

function sortProducts() {
    // Basic JavaScript to sort products
    console.log("Sorting products (functionality to be implemented)");
}

function addToCart(button) {
    // Example add to cart functionality
    alert("Added to cart!");
    // Further code to actually add the product to a cart goes here
}

function buyNow(button) {
    // Example buy now functionality
    alert("Proceed to checkout!");
    // Further code to actually buy the product goes here
}
function searchProducts() {
    var searchTerm = document.getElementById('searchBox').value;
    alert('Searching for: ' + searchTerm);

    // Intentionally vulnerable to XSS
    document.getElementById('searchResults').innerHTML = "Results for: " + searchTerm;
}

// Existing functions for sorting, adding to cart, etc., if any
