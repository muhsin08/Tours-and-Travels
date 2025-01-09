from django.db import models
from user_app.models import *
# Create your models here.
class restaurant_model(models.Model):
    bussiness_name = models.CharField(max_length=20, null=True, blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    resturent = models.OneToOneField(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    phone_number=models.IntegerField(null=True,blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField(null=True,blank=True)
    capacity = models.IntegerField(null=True,blank=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    connect = models.ForeignKey(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    lock = models.ForeignKey(restaurant_model, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'Appetizer'),  # Appetizers like snacks, small starters
        ('main_course', 'Main Course'),  # Main dishes, larger servings
        ('dessert', 'Dessert'),  # Sweet dishes served after the main course
        ('beverage', 'Beverage'),  # Drinks, soft drinks, etc.
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    connect = models.ForeignKey(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    lock = models.ForeignKey(restaurant_model, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class mycomplaints(models.Model):
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    reply = models.TextField(null=True, blank=True)
    reply_date = models.DateField(null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
