from django.urls import path
from dashboard import views as dashboard




app_name = 'dashboard'
urlpatterns = [
  path('dashboard/', dashboard.dashboard_page, name="dashboard_page"),




  path('addemployee/', dashboard.add_employee, name="add_employee"),
  path('employees/', dashboard.list_employee, name="list_employee"),
  path('employee/update/<int:id>', dashboard.update_employee, name="update_employee"),
  path('employee/delete/<int:id>', dashboard.delete_employee, name="delete_employee"),




  path('medicine/', dashboard.medicine_list_admin, name="medicine_list_admin"),
  path('medicine/delete/<int:id>', dashboard.delete_medicine, name="delete_medicine"),
  path('medicine/update/<int:id>', dashboard.update_medicine, name="update_medicine"),
  path('medicine/add/', dashboard.add_medicine, name="add_medicine"),




  path('faq/', dashboard.faq_list, name="faq_list"),
  path('faq/add/', dashboard.faq_add, name="faq_add"),




  path('upload/prescription/', dashboard.upload_prescription, name="upload_prescription"),
  path('prescription/<int:id>/update', dashboard.update_prescription, name="update_prescription"),
  path('prescription/', dashboard.presciption_list_admin, name="presciption_list_admin"),
 
  path('notification/add/', dashboard.add_notification, name="add_notification"),
 
  path('sales/', dashboard.sales_list, name="sales_list"),
  path('sales/add/', dashboard.add_sales, name="add_sales"),
  path('sales/<int:id>/update/', dashboard.update_sales, name="update_sales"),
 
  path("bills/", dashboard.list_bill, name="list_bill"),
  path("bills/add/", dashboard.generate_bill, name="generate_bill"),
  path("bills/update/<int:id>/", dashboard.update_bill, name="update_bill"),


  path("billitem/<int:bill_id>/", dashboard.bill_item_list, name="bill_item_list"),
  path("billitem/<int:bill_id>/add/", dashboard.generate_bill_items, name="generate_bill_items"),
  path("billitem/<int:bill_id>/delete/<int:item_id>/", dashboard.delete_bill_item, name="delete_bill_item"),


  path("cbills/<int:app_id>", dashboard.customer_bills, name="customer_bills"),
 
  path("search/", dashboard.search_by_email, name="search_by_email"),
]



