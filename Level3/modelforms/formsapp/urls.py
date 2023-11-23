from django.urls import path
from formsapp import views

urlpatterns = [
    path('',views.users,name='users'),

]