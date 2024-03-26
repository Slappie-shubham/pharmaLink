from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Medicine
from dashboard.forms import EmployeeRegisterForm, EmployeeUpdateForm
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
            return redirect("dashboard:list_employee")
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

@login_required(login_url='/')
def delete_employee(request, id):
    employee = User.objects.filter(is_employee=True, id=id).first()
    employee.delete()
    return redirect("dashboard:list_employee")


@login_required(login_url='/')
def update_employee(request, id):

    employee = User.objects.filter(is_employee=True, id=id).first()
    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_employee = True
            user.username = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Successfully Updated Employee")
            return redirect("dashboard:list_employee")
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, "dashboard/employee/update.html", {'form': form})


@login_required(login_url='/')
def medicine_list_admin(request):
    medicine = Medicine.objects.all()
    return render(request, "dashboard/medicine/list.html", {"medicine" : medicine})

@login_required(login_url='/')
def delete_medicine(request, id):
    medicine = Medicine.objects.filter(id=id).first()
    medicine.delete()
    return redirect("dashboard:medicine_list_admin")




