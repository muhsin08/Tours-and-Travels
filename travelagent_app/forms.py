from django import forms
from .models import *


class travelagent_form(forms.ModelForm):
    class Meta:
        model=travelagent_model
        fields=['phone_number','bussiness_name','tax_identification_number']
class packages_form(forms.ModelForm):
    class Meta:
        model=travel_package
        fields=['name','description','price','duration_days','available_from','available_to','package_type',
               'destinations','image']
class complaint_agents(forms.ModelForm):
    class Meta:
        model=complaints
        fields=['message','date']
class reply_complaints(forms.ModelForm):
    class Meta:
        model=complaints
        fields=['reply','reply_date']
