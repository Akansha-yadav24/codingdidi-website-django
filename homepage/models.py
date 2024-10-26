from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's password hashing
    # Add additional fields as necessary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
