from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
#         ROLE_CHOICES = [
#                 ('buyer', 'Buyer'),
#                 ('seller', 'Seller'),
#         ]
#
#         user = models.OneToOneField(User, on_delete=models.CASCADE)
#         full_name = models.CharField(max_length=100)
#         email = models.EmailField(unique=True)
#         role = models.CharField(max_length=10, choices=ROLE_CHOICES)
#         password = models.CharField(max_length=255)
#         firebase_user_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
#         created_at = models.DateTimeField(auto_now_add=True)
#         profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#
#
#         def __str__(self):
#                 return self.email


class FirebaseUser(models.Model):
        uid = models.CharField(max_length=100, unique=True)  # Firebase User ID
        full_name = models.CharField(max_length=255)
        email = models.EmailField(unique=True)
        role = models.CharField(max_length=20, choices=[('buyer', 'Buyer'), ('seller', 'Seller')])
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
                return f"{self.full_name} ({self.email})"
