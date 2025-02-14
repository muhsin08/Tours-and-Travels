from django import forms
from .models import *
class restaurant_form(forms.ModelForm):
    class Meta:
        model=restaurant_model
        fields=['bussiness_name','phone_number','image','latitude','longitude']
class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=['image','number','category','description','capacity','price_per_night','facilities']




class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'category', 'image','availability']
class review_forms(forms.ModelForm):
    class Meta:
        model=Review
        fields=['rating','comment']
class rest_complaintform(forms.ModelForm):
    class Meta:
        model=mycomplaints
        fields=['message','date']
class replyform(forms.ModelForm):
    class Meta:
        model=mycomplaints
        fields=['reply','reply_date']
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'check_in_date', 'check_out_date','number_of_guests','total_price']
class Bookdish_Form(forms.ModelForm):
    class Meta:
        model = BookDish
        fields = ['quantity', 'booking_date', 'special_requests']


