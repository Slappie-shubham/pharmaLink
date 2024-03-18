from django.urls import path
from dashboard import views as dashboard

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', dashboard.dashboard_page, name="dashboard_page"),
    path('addemployee/', dashboard.add_employee, name="add_employee"),
]
