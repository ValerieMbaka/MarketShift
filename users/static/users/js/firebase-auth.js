// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-analytics.js";

// Import Firebase Authentication SDK
import firebase from 'https://www.gstatic.com/firebasejs/9.1.2/firebase-app.js';
import 'https://www.gstatic.com/firebasejs/9.1.2/firebase-auth.js';

// Firebase configuration (replace with your Firebase project configuration)
const firebaseConfig = {
        apiKey: "AIzaSyCGUC9u38j5Oj9YlarABz8aicybX39wyCQ",
        authDomain: "web-development-fe6af.firebaseapp.com",
        projectId: "web-development-fe6af",
        storageBucket: "web-development-fe6af.firebasestorage.app",
        messagingSenderId: "647043206129",
        appId: "1:647043206129:web:8d9293e224889766dc1250",
        measurementId: "G-E64SJZXZED"
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);
const auth = firebase.auth(app);

// Handle Firebase Authentication (Login)
const handleLogin = async (email, password) => {
    try {
        const userCredential = await auth.signInWithEmailAndPassword(email, password);
        const user = userCredential.user;

        // Get the ID token after the user is logged in
        const idToken = await user.getIdToken(true);

        // Send the ID token to the backend (Django)
        await sendTokenToBackend(idToken, email, password);

    } catch (error) {
        console.error("Error during login:", error);
    }
};

// Send the ID token to the Django backend for further validation
const sendTokenToBackend = async (idToken, email, password) => {
    try {
        const response = await fetch('/login/', {
            method: 'POST',
            body: JSON.stringify({
                id_token: idToken,
                email: email,
                password: password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();

        if (data.success) {
            console.log("User authenticated successfully");
            // You can redirect the user after a successful login
            window.location.href = "/dashboard";  // Change this to your desired redirect page
        } else {
            console.log("Login failed:", data.message);
        }

    } catch (error) {
        console.error("Error sending token to backend:", error);
    }
};

// Listen for login form submission
document.getElementById("login-form").addEventListener("submit", (e) => {
    e.preventDefault();

    const email = e.target.email.value;
    const password = e.target.password.value;

    // Call the handleLogin function with the form data
    handleLogin(email, password);
});
