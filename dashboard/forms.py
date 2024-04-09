from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from dashboard.models import *




class EmployeeRegisterForm(UserCreationForm):
  class Meta:
      model = User
      fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob', 'password1', 'password2')




class EmployeeUpdateForm(forms.ModelForm):  
  class Meta:
      model = User
      fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'dob')




class StocksUpdateForm(forms.ModelForm):
   manufacture_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))  
   expiry_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))  
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
      fields = ('prescription', 'customer_notes')
    
class DoctorsPrescriptioncustomerUpdateForm(forms.ModelForm):
  class Meta:
      model = DoctorsPrescription
      fields = ('prescription', 'customer_notes')


class DoctorsPrescriptionemployeeUpdateForm(forms.ModelForm):
  class Meta:
      model = DoctorsPrescription
      fields = ('employee_notes','status')
     
     
class AddNotification(forms.ModelForm):
  class Meta:
      model = Notification
      fields = ('specific_user','notification')