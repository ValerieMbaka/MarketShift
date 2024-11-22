from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import auth, credentials, firestore
from django.contrib import messages
from .models import  FirebaseUser
# from .models import  UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.core.files.storage import FileSystemStorage

# Import the random password generation function
import secrets
import string


# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate(
                'C:/Users/user/OneDrive/Documents/Firebase/web-development-fe6af-firebase-adminsdk-chwhp-bea71374ea.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()

# Create your views here.
def index(request):
        return render(request, 'index.html')

def signup(request):
        if request.method == 'POST':
                full_name = request.POST['full_name']
                email = request.POST['email']
                role = request.POST['role']
                password = request.POST['password']
                password_confirmation = request.POST['password_confirmation']

                # Basic validation
                if not all([full_name, email, role, password, password_confirmation]):
                        messages.error(request, "All fields are required.")
                        return render(request, "signup.html")

                if password != password_confirmation:
                        messages.error(request, "Passwords do not match.")
                        return render(request, "signup.html")

                if len(password) < 6:
                        messages.error(request, "Password must be at least 6 characters long.")
                        return render(request, "signup.html")

                try:
                        # Create user in Firebase Authentication
                        user = auth.create_user(
                                email=email,
                                password=password,
                                display_name=full_name,
                        )

                        # Generate email verification link
                        link = auth.generate_email_verification_link(email)

                        # Now you have to send this link to the user via email.
                        # For simplicity, you can use your Django backend or a third-party email service to send this link.

                        # For example, you could use Django's send_mail() or an external service like SendGrid.
                        send_verification_email(email, link)  # You need to implement this function for email sending

                        # Save role in Firestore or user metadata
                        db.collection('users').document(user.uid).set({
                                'full_name': full_name,
                                'email': email,
                                'role': role,
                        })

                        # Sync with local FirebaseUser model
                        FirebaseUser.objects.create(
                                uid=user.uid,
                                full_name=full_name,
                                email=email,
                                role=role
                        )

                        messages.success(request, "Account created successfully!")
                        # Redirect based on role
                        if role == 'buyer':
                                messages.success(request, "Welcome, Buyer!")
                                return redirect("/buyer/dashboard/")
                        elif role == 'seller':
                                messages.success(request, "Welcome, Seller!")
                                return redirect("/seller/dashboard/")
                        else:
                                messages.error(request, "Unknown role selected.")
                                return render(request, "signup.html")

                except Exception as e:
                        messages.error(request, f"Error: {e}")
                        return render(request, "signup.html")

        return render(request, 'signup.html')


# A placeholder for the email sending function (you need to implement this)
def send_verification_email(email, link):
        from django.core.mail import send_mail
        send_mail(
        'Email Verification',
        f'Please verify your email by clicking the following link: {link}',
        'from@example.com',  # You can set a custom email here
        [email],
                fail_silently=False,
        )


def buyer_dashboard(request):
        return render(request, "buyer_dashboard.html", {"message": "Welcome to the Buyer Dashboard!"})

def seller_dashboard(request):
        return render(request, "seller_dashboard.html", {"message": "Welcome to the Seller Dashboard!"})

