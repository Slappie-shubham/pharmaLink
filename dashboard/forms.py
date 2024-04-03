from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from dashboard.models import Stocks, FAQ, DoctorsPrescription

class EmployeeRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob', 'password1', 'password2')

class EmployeeUpdateForm(forms.ModelForm):    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob')

class StocksUpdateForm(forms.ModelForm):    
    class Meta:
        model = Stocks
        fields = ('name', 'generic_name', 'dosage_strength', 'dose_form', 'manufacture_name', 'manufacture_date', 'stock', 'batch', 'expiry_date','extra_detail')

class FaqAddForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', 'answer')
        
class DoctorsPrescriptionAddForm(forms.ModelForm):
    class Meta:
        model = DoctorsPrescription
        fields = ('prescription', 'notes')
        




