from django import forms
from .models import *


class travelagent_form(forms.ModelForm):
    class Meta:
        model=travelagent_model
        fields=['phone_number','bussiness_name','tax_identification_number','image']
class packages_form(forms.ModelForm):
    class Meta:
        model=travel_package
        fields=['name','description','price','duration_days','available_from','available_to','package_type',
               'destinations','image']
class travel_complaintform(forms.ModelForm):
    class Meta:
        model=Complaints
        fields=['message','date']
class reply_form(forms.ModelForm):
    class Meta:
        model=Complaints
        fields=['reply','reply_date']
class reviewforms(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['rating','comment']
class packbook_form(forms.ModelForm):
    class Meta:
        model=Booking_package
        fields=['number_of_people','booking_date','total_amount','travel_dates']
class pyment_form(forms.ModelForm):
    class Meta:
        model=Payment
        fields=['amount','payment_method','payment_date']

