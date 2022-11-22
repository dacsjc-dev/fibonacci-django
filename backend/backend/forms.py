from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile as UserProfileModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfileModel
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfileModel
        fields = ("username", "email")