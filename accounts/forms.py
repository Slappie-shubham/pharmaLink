from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm
from dashboard.models import Medicine

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

class CustomPasswordChangeForm(PasswordChangeForm):
    pass

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


