from django.urls import path
from accounts import views as accounts




app_name = 'accounts'
urlpatterns = [
   path('', accounts.login_page, name="login_page"),


   path('register/', accounts.register_page, name="register_page"),
   path('register/success', accounts.registration_success, name="register_success"),
   path('activation/success', accounts.activation_success, name="activation_success"),


   path('logout/', accounts.logout_process, name="logout_process"),


   path('change_password/', accounts.change_password, name="change_password"),
   path('activate/<str:uidb64>/<str:token>/', accounts.activate_user, name='activate_user'),
   
   path('profile/', accounts.list_profile, name='list_profile'),
   path('profile/update/', accounts.update_profile, name='update_profile'),


  






]
