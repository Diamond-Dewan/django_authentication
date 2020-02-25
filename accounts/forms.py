from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=225, help_text='Add a valid E-mail address', required=True, error_messages={'required': 'Please enter a valid E-mail address'})
    first_name = forms.CharField(max_length=100, help_text='First Name', required=False)
    last_name = forms.CharField(max_length=100, help_text='Last Name', required=False)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

