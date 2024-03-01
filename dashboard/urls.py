from django.urls import path
from dashboard import views as dashboard

app_name = 'accounts'
urlpatterns = [
    path('dashboard/', dashboard.dashboard_page, name="dashboard_page"),
]
