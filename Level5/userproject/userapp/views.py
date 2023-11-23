from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from userapp.forms import UserForm,UserProfileInfoForm



from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request,'userapp/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        userForm = UserForm(request.POST)
        profileForm = UserProfileInfoForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        
        else:
            print(userForm.errors,profileForm.errors)
    else:
        userForm = UserForm()
        profileForm = UserProfileInfoForm()
    
    return render(request,'userapp/register.html',{
        'userForm': userForm, 'profileForm':profileForm, 'registered': registered
    })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                
            else:
                return HttpResponse('Account not Active')
            
        else:
            HttpResponse('Looks like your Username or Password is wrong!')
    
    else:
        return render(request,'userapp/login.html')
