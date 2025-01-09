from .models import User_profile
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User_profile
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User_profile
        exclude = []