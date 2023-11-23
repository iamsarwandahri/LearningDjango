from django.shortcuts import render


mydict = {'index':'Home','ot':'Other','lead':'Admin','time':'Relative'}
def index(request):
    return render(request,'templatesapp/index.html',mydict)

def other(request):
    return render(request,'templatesapp/other.html',mydict)

def relative(request):
    return render(request,'templatesapp/relative.html',mydict)

def basic(request):
    return render(request,'templatesapp/basic.html',mydict)