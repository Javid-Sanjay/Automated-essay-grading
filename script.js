
document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Get input values
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;

    // Perform login validation (add your own validation logic here)
    var isValid = validateLogin(username, email);

    if (isValid) {
        // Redirect to essay.html after successful login
        window.location.href = "essay.html";
    } else {
        // Show error message or perform appropriate action
        alert("Invalid login credentials. Please try again.");
    }
});

function validateLogin(username, email) {
    // Add your login validation logic here
    // You can perform checks like verifying against a database or any other authentication mechanism
    // For this example, we'll consider the login as valid if both fields are non-empty

    return username.trim() !== "" && email.trim() !== "";
}
