from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Medicine
from dashboard.forms import EmployeeRegisterForm, EmployeeUpdateForm, MedicineUpdateForm
from django.contrib import messages
from accounts.models import User
from django.utils import timezone



# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
    medicine = Medicine.objects.all()
    users_count = User.objects.filter(is_customer=True).count()
    medicine_count = Medicine.objects.all().count()
    expired_medicine_count = Medicine.objects.filter(expiry_date__lt=timezone.now()).count()

    jan_medicine = Medicine.objects.filter(created_date__month=1).count()
    feb_medicine = Medicine.objects.filter(created_date__month=2).count()
    mar_medicine = Medicine.objects.filter(created_date__month=3).count()
    apr_medicine = Medicine.objects.filter(created_date__month=4).count()
    may_medicine = Medicine.objects.filter(created_date__month=5).count()
    june_medicine = Medicine.objects.filter(created_date__month=6).count()
    july_medicine = Medicine.objects.filter(created_date__month=7).count()
    aug_medicine = Medicine.objects.filter(created_date__month=8).count()
    sep_medicine = Medicine.objects.filter(created_date__month=9).count()
    oct_medicine = Medicine.objects.filter(created_date__month=10).count()
    nov_medicine = Medicine.objects.filter(created_date__month=11).count()
    dec_medicine = Medicine.objects.filter(created_date__month=12).count()
    context = {
        'medicine' : medicine,
        'users_count' : users_count,
        'medicine_count' : medicine_count,
        'expired_medicine_count' : expired_medicine_count,
        'jan_medicine' : jan_medicine,
        'feb_medicine' : feb_medicine,
        'mar_medicine' : mar_medicine,
        'apr_medicine' : apr_medicine,
        'may_medicine' : may_medicine,
        'june_medicine' : june_medicine,
        'july_medicine' : july_medicine,
        'aug_medicine' : aug_medicine,
        'sep_medicine' : sep_medicine,
        'oct_medicine' : oct_medicine,
        'nov_medicine' : nov_medicine,
        'dec_medicine' : dec_medicine,
        
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


@login_required(login_url='/')
def update_medicine(request, id):

    medicine = Medicine.objects.filter(id=id).first()
    if request.method == "POST":
        form = MedicineUpdateForm(request.POST, instance=medicine)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.save()
            messages.success(request, "Successfully Updated Medicine")
            return redirect("dashboard:medicine_list_admin")
    else:
        form = MedicineUpdateForm(instance=medicine)
    return render(request, "dashboard/medicine/update.html", {'form': form})

@login_required(login_url='/')
def add_medicine(request):
    if request.method == "POST":
        form = MedicineUpdateForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.save()
            messages.success(request, "Successfully Added Medicine")
            return redirect("dashboard:medicine_list_admin")
    else:
        form = MedicineUpdateForm()
    return render(request, 'dashboard/medicine/add.html', {'form': form})