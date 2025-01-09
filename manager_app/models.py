from django.db import models
from django.db import models
from user_app.models import *
from travelagent_app .models import *
from customer_app .models import *
# Create your models here.
class add_turistplaces(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    discription=models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='upload images/', null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)




class  add_Spot(models.Model):
    CATEGORY_CHOICES = [
        ('outdoor', 'Outdoor'),
        ('indoor', 'Indoor'),
        ('studio', 'Studio'),
        ('event', 'Event'),
    ]

    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=300,null=True,blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='upload images/', blank=True, null=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Festival(models.Model):

    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    image = models.ImageField(upload_to='upload images/', blank=True, null=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class VR_vedios(models.Model):
    tourist_spot = models.ForeignKey(add_Spot,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    video_file = models.FileField(upload_to='vr_videos/', null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class hotel(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    image = models.ImageField(upload_to='upload images/', null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class send_feedback(models.Model):
    user=models.ForeignKey(User_profile,on_delete=models.CASCADE,null=True,blank=True)
    content=models.CharField(max_length=300,null=True,blank=True)
    title=models.CharField(max_length=30,null=True,blank=True)
    reply=models.CharField(max_length=300,null=True,blank=True)
    reply_date=models.DateField(null=True,blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
class booking(models.Model):
    packageid=models.ForeignKey(travel_package,on_delete=models.CASCADE,blank=True,null=True)
    accountnumber=models.IntegerField(null=True,blank=True)
    booking_date=models.DateField(null=True,blank=True)
    name_details=models.TextField(null=True,blank=True)
    connect = models.ForeignKey(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    lock = models.ForeignKey(customer_model, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

