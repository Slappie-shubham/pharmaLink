from django.urls import path
from dashboard import views as dashboard

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', dashboard.dashboard_page, name="dashboard_page"),
    path('addemployee/', dashboard.add_employee, name="add_employee"),
    path('employees/', dashboard.list_employee, name="list_employee"),
    path('employee/update/<int:id>', dashboard.update_employee, name="update_employee"),
    path('employee/delete/<int:id>', dashboard.delete_employee, name="delete_employee"),
]
