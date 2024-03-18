from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class EmployeeRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob', 'password1', 'password2')







