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
]
