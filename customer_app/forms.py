from django import forms
from .models import *


class customer_form(forms.ModelForm):
    class Meta:
        model=customer_model
        fields=['full_name','phone_number']