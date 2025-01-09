from django.db import models
from user_app.models import *
from travelagent_app.models import *
# Create your models here.
class customer_model(models.Model):
    full_name=models.CharField(max_length=20,null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    customer = models.OneToOneField(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)