from django.db import models
from user_app.models import *
# Create your models here.
class travelagent_model(models.Model):
    phone_number=models.IntegerField(null=True,blank=True)
    bussiness_name=models.CharField(max_length=20,null=True,blank=True)
    travelagent = models.OneToOneField(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    tax_identification_number=models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class travel_package(models.Model):
    PACKAGE_TYPES = [
        ('family', 'Family'),
        ('luxury', 'Luxury'),
        ('honeymoon', 'Honeymoon'),
        ('adventure', 'Adventure'),
    ]

    name=models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(null=True,blank=True)
    available_from = models.DateField()
    available_to = models.DateField()
    package_type = models.CharField(max_length=50, choices=PACKAGE_TYPES)
    destinations = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to='upload images/')
    connect=models.ForeignKey(User_profile,on_delete=models.CASCADE,blank=True,null=True)
    lock=models.ForeignKey(travelagent_model,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class complaints(models.Model):
    user=models.ForeignKey(User_profile,on_delete=models.CASCADE,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    reply=models.TextField(null=True,blank=True)
    reply_date=models.DateField(null=True,blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


