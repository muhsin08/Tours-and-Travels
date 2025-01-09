from django import forms
from .models import *

class turistplace_form(forms.ModelForm):
    class Meta:
        model=add_turistplaces
        fields=['name','discription','image']

class SpotForm(forms.ModelForm):
    class Meta:
        model = add_Spot
        fields = ['name', 'description', 'location', 'category', 'image']
class festival_form(forms.ModelForm):
    class Meta:
        model=Festival
        fields=['name','description','location','start_date','end_date','start_time','end_time','image']
class VR_videosform(forms.ModelForm):
    class Meta:
        model=VR_vedios
        fields=['tourist_spot','title','video_file','description']
class hotel_form(forms.ModelForm):
    class Meta:
        model=hotel
        fields=['name','description','address','phone_number','email','rating','image']
class feedbackform(forms.ModelForm):
    class Meta:
        model=send_feedback
        fields=['content','title']
class replyform(forms.ModelForm):
    class Meta:
        model=send_feedback
        fields = ['reply', 'reply_date']
class booking_forms(forms.ModelForm):
    class Meta:
        model=booking
        fields=['packageid','accountnumber','booking_date','name_details']
# class place_searchform(forms.ModelForm):
#     class Meta:
#         model=add_turistplaces
        