from django.urls import path
from accounts import views as accounts
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('', accounts.login_page, name="login_page"),
    path('register/', accounts.register_page, name="register_page"),
    path('logout/', accounts.logout_process, name="logout_process"),



    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
