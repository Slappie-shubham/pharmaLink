from django.urls import path
from accounts import views as accounts

app_name = 'accounts'
urlpatterns = [
    path('', accounts.login_page, name="login_page"),
    path('register/', accounts.register_page, name="register_page"),
    path('logout/', accounts.logout_process, name="logout_process"),
]
