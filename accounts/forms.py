from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm




class UserRegisterForm(UserCreationForm):
   class Meta:
       model = User
       fields = ('email', 'password1', 'password2', 'first_name', 'last_name')


class CustomPasswordChangeForm(PasswordChangeForm):
   pass






class updateProfile(forms.ModelForm):
   dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
   class Meta:
       model = User
       fields = ('first_name','last_name','address','phone','profile_pic','dob')