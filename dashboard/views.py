from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Medicine
from dashboard.forms import EmployeeRegisterForm
from django.contrib import messages
from accounts.models import User

# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
    medicine = Medicine.objects.all()
    context = {
        'medicine' : medicine
    }
    return render(request,'dashboard/dashboard.html', context)

@login_required(login_url='/')
def add_employee(request):
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_employee = True
            user.username = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Successfully Added Employee")
    else:
        form = EmployeeRegisterForm()
    return render(request, 'dashboard/employee/add.html', {'form': form})

@login_required(login_url='/')
def list_employee(request):
    employee = User.objects.filter(is_employee=True)
    context = {
        'employees' : employee
    }
    return render(request, "dashboard/employee/list.html", context)




