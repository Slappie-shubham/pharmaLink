from django.urls import path
from accounts import views as accounts

app_name = 'accounts'
urlpatterns = [
    path('', accounts.login_page, name="login_page"),
]
