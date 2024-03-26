from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from dashboard.models import Medicine

class EmployeeRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob', 'password1', 'password2')

class EmployeeUpdateForm(forms.ModelForm):    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob')

# class MedicineUpdateForm(forms.ModelForm):    
#     class Meta:
#         model = Medicine
#         fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob')






