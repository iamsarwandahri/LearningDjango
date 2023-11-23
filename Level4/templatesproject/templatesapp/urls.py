from django.urls import path
from templatesapp import views

app_name = 'templatesapp'

urlpatterns = [
    path('',views.basic,name='basic'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]