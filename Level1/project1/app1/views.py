from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    dic = {'insert_me':"I am Sarwan's Page"}
    return render(request,'app1/index.html',context=dic)