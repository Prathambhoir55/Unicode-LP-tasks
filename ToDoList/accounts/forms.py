from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number', 'birth_date', 'user_image')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'mobile_number', 'birth_date', 'user_image')