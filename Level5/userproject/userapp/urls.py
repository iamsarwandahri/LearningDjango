from django.urls import path
from userapp import views


app_name = 'userapp'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.user_login,name='login'),
]