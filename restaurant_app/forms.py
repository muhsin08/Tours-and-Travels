from django import forms
from .models import *
class restaurant_form(forms.ModelForm):
    class Meta:
        model=restaurant_model
        fields=['bussiness_name','location','phone_number']
class complaint_rest(forms.ModelForm):
    class Meta:
        model=mycomplaints
        fields=['message','date']
class reply_mycomplaints(forms.ModelForm):
    class Meta:
        model=mycomplaints
        fields=['reply','reply_date']

class RoomFacilitiesForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'floor', 'capacity', 'description']
class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'category', 'image',]
