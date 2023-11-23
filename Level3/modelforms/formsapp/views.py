from django.shortcuts import render
from formsapp import views
# from formsapp.models import User
from formsapp.forms import NewUserForm

def index(request):
    dic = {'Name':'Sarwan'}
    return render(request,'html/index.html',context=dic)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Nothing Found')

    return render(request,'html/users.html',{'form':form})