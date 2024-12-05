from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Extend the built-in User model
class User(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('client', 'Client User'),
        ('business', 'Business User'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)

# Store Model for Business Users
class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Business User Profile
class BusinessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='business_users')
    admin = models.BooleanField(default=False) 

    def __str__(self):
        return f"Business User: {self.user.username} - Store: {self.store.name} - Admin: {self.admin}"

# Client User Profile
class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    # preferences = models.TextField(blank=True, null=True)  # Example field for client-specific data

    def __str__(self):
        return f"Client User: {self.user.username}"