from django.shortcuts import render
from app2 import views
from app2.models import Student

def index(request):
    dic = {'Name':'Sarwan'}
    return render(request,'html/index.html',context=dic)

def users(request):
    stu = Student.objects.all()
    mydict = {'stu':stu}
    return render(request,'html/users.html',context=mydict)