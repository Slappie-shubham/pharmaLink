from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Stocks, FAQ, DoctorsPrescription
from dashboard.forms import *
from django.contrib import messages
from accounts.models import User
from django.utils import timezone
from datetime import date


# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
 medicine = Stocks.objects.all()
 today = date.today() 
 medicine_expire = Stocks.objects.filter(expiry_date__lt=today)
 users_count = User.objects.filter(is_customer=True).count()
 medicine_count = Stocks.objects.all().count()
 expired_medicine_count = Stocks.objects.filter(expiry_date__lt=timezone.now()).count()
 prescription = DoctorsPrescription.objects.filter(user=request.user).order_by('-id')




 jan_medicine = Stocks.objects.filter(created_date__month=1).count()
 feb_medicine = Stocks.objects.filter(created_date__month=2).count()
 mar_medicine = Stocks.objects.filter(created_date__month=3).count()
 apr_medicine = Stocks.objects.filter(created_date__month=4).count()
 may_medicine = Stocks.objects.filter(created_date__month=5).count()
 june_medicine = Stocks.objects.filter(created_date__month=6).count()
 july_medicine = Stocks.objects.filter(created_date__month=7).count()
 aug_medicine = Stocks.objects.filter(created_date__month=8).count()
 sep_medicine = Stocks.objects.filter(created_date__month=9).count()
 oct_medicine = Stocks.objects.filter(created_date__month=10).count()
 nov_medicine = Stocks.objects.filter(created_date__month=11).count()
 dec_medicine = Stocks.objects.filter(created_date__month=12).count()
 context = {
     'medicine' : medicine,
     'medicine_expire' : medicine_expire,
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
     'prescription' : prescription,
  
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
 medicine = Stocks.objects.all()
 return render(request, "dashboard/medicine/list.html", {"medicine" : medicine})








@login_required(login_url='/')
def delete_medicine(request, id):
 medicine = Stocks.objects.filter(id=id).first()
 medicine.delete()
 return redirect("dashboard:medicine_list_admin")
















@login_required(login_url='/')
def update_medicine(request, id):








 medicine = Stocks.objects.filter(id=id).first()
 if request.method == "POST":
     form = StocksUpdateForm(request.POST, instance=medicine)
     if form.is_valid():
         medicine = form.save(commit=False)
         medicine.save()
         messages.success(request, "Successfully Updated Medicine")
         return redirect("dashboard:medicine_list_admin")
 else:
     form = StocksUpdateForm(instance=medicine)
 return render(request, "dashboard/medicine/update.html", {'form': form})








@login_required(login_url='/')
def add_medicine(request):
 if request.method == "POST":
     form = StocksUpdateForm(request.POST)
     if form.is_valid():
         medicine = form.save(commit=False)
         medicine.save()
         messages.success(request, "Successfully Added Medicine")
         return redirect("dashboard:medicine_list_admin")
 else:
     form = StocksUpdateForm()
 return render(request, 'dashboard/medicine/add.html', {'form': form})








@login_required(login_url='/')
def faq_list(request):
 faq = FAQ.objects.all()
 return render(request, "dashboard/faq/list.html", {'faq': faq})








@login_required(login_url='/')
def faq_add(request):
 if request.method == "POST":
     form = FaqAddForm(request.POST)
     if form.is_valid():
         form.save()
         messages.success(request, "Successfully Added FAQ")
         return redirect("dashboard:faq_list")
 else:
     form = FaqAddForm()
 return render(request, 'dashboard/faq/add.html', {'form': form})
















@login_required(login_url='/')
def upload_prescription(request):
 if request.method == "POST":
     form = DoctorsPrescriptionAddForm(request.POST, request.FILES)
     if form.is_valid():
         prescription = form.save(commit=False)
         prescription.user = request.user
         prescription.save()
         Notification.objects.create(notification="New pescription has been posted", created_by=request.user, specific_user=User.objects.filter(is_employee=True).first())
         messages.success(request, "Successfully Uploaded")
         return redirect("dashboard:dashboard_page")
 else:
     form = DoctorsPrescriptionAddForm()
 return render(request, 'dashboard/prescription/add.html', {'form': form})
















@login_required(login_url='/')
def update_prescription(request, id):
 presciption = DoctorsPrescription.objects.filter(id=id).first()
 if request.method == "POST":
     if request.user.is_customer:
         form = DoctorsPrescriptioncustomerUpdateForm(request.POST, instance=presciption)
     if request.user.is_employee:
         form = DoctorsPrescriptionemployeeUpdateForm(request.POST, instance=presciption)
     if form.is_valid():
         pre = form.save(commit=False)
         pre.user = request.user
         pre.save()
         messages.success(request, "Successfully Updated presciption")
         return redirect("dashboard:dashboard_page")
 else:
     if request.user.is_customer:
         form = DoctorsPrescriptioncustomerUpdateForm(instance=presciption)
     if request.user.is_employee:
         form = DoctorsPrescriptionemployeeUpdateForm(instance=presciption)
 return render(request, "dashboard/prescription/update.html", {'form': form})








@login_required(login_url='/')
def presciption_list_admin(request):
 prescription = DoctorsPrescription.objects.all().order_by('-id')
 return render(request, "dashboard/prescription/list.html", {'prescription': prescription})












@login_required(login_url='/')
def add_notification(request):
  if request.method == "POST":
      form = AddNotification(request.POST)
      if form.is_valid():
          notif = form.save(commit=False)
          notif.created_by = request.user
          notif.save()
          messages.success(request, "Successfully Added Notification")
          print('-----------------------------------')
          return redirect("dashboard:dashboard_page")
  else:
      form = AddNotification()
  return render(request, 'dashboard/notification/add.html', {'form': form})
@login_required(login_url='/')
def sales_list(request):
 sales = Sales.objects.all()
 return render(request, "dashboard/sales/list.html", {"sales" : sales})


# @login_required(login_url='/')
# def delete_sales(request, id):
#   medicine = Sales.objects.filter(id=id).first()
#   medicine.delete()
#   return redirect("dashboard:sales_list")




@login_required(login_url='/')
def update_sales(request, id):


 medicine = Sales.objects.filter(id=id).first()
 if request.method == "POST":
     form = SalesForm(request.POST, instance=medicine)
     if form.is_valid():
         medicine = form.save(commit=False)
         medicine.save()
         messages.success(request, "Successfully Updated sales")
         return redirect("dashboard:sales_list")
 else:
     form = SalesForm(instance=medicine)
 return render(request, "dashboard/sales/update.html", {'form': form})


@login_required(login_url='/')
def add_sales(request):
 if request.method == "POST":
     form = SalesForm(request.POST)
     if form.is_valid():
         medicine = form.save(commit=False)
         medicine.save()
         messages.success(request, "Successfully Added sales")
         return redirect("dashboard:sales_list")
 else:
     form = SalesForm()
 return render(request, 'dashboard/sales/add.html', {'form': form})


@login_required(login_url='/')
def generate_bill(request):
   if request.method == 'POST':
       form = GenerateBillForm(request.POST)
       if form.is_valid():
           data = form.save(commit=False)
           data.generated_by = request.user
           data.save()
           messages.success(request, "Successfully generated bill")
           return redirect("dashboard:dashboard_page")
   else:
       form = GenerateBillForm()
   return render(request, 'dashboard/bills/add.html', {'form': form})


@login_required(login_url='/')
def update_bill(request, id):
   bill = Bills.objects.filter(id=id).first()
   if request.method == 'POST':
       form = GenerateBillForm(request.POST, instance=bill)
       if form.is_valid():
           data = form.save(commit=False)
           data.generated_by = request.user
           data.save()
           messages.success(request, "Successfully updated bill")
           return redirect("dashboard:list_bill")
   else:
       form = GenerateBillForm(instance=bill)
   return render(request, "dashboard/bills/update.html", {'form': form})


@login_required(login_url='/')
def list_bill(request):
   bill = Bills.objects.all()
   context = {
       'bill': bill
       }
   return render(request,"dashboard/bills/list.html", context)


@login_required(login_url='/')
def generate_bill_items(request, bill_id):
   if request.method == 'POST':
       form = AddBillItemForm(request.POST)
       mainbill = Bills.objects.get(id=bill_id)
       if form.is_valid():
           bill = form.save(commit=False)
           bill.bills = mainbill
           bill.save()
           messages.success(request, "Successfully added items bill")
           return redirect("dashboard:bill_item_list", bill_id=bill_id)
   else:
       form = AddBillItemForm()
   return render(request, 'dashboard/bills/item/add.html', {'form': form})


@login_required(login_url='/')
def bill_item_list(request, bill_id):
   mainbill = Bills.objects.get(id=bill_id)
   billitem = BillsItems.objects.filter(bills=mainbill)
   context = {
       'billitem': billitem,
       'bill_id': bill_id,
       }
   return render(request,"dashboard/bills/item/list.html", context)


@login_required(login_url='/')
def delete_bill_item(request, bill_id, item_id):
   billitem = BillsItems.objects.filter(id=item_id).first()
   billitem.delete()
   messages.success(request, "Successfully deleted items bill")
   return redirect("dashboard:bill_item_list", bill_id=bill_id)




@login_required(login_url='/')
def customer_bills(request, app_id):
   cbill = Bills.objects.filter(prescription=app_id).first()
   context = {
       'cbill': cbill
       }
   return render(request,"dashboard/bills/customer_bill.html", context)




@login_required(login_url='/')
def search_by_email(request):
   context = {}
   if request.method == 'GET':
       email = request.GET.get('email')
       if email:
           cbills = Bills.objects.filter(generated_by__email=email)
           context['cbills'] = cbills
   return render(request, "dashboard/search/search.html", context)

