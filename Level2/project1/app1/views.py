from django.shortcuts import render
from app1.models import Topic,Webpage,AccessRecords


def index(request):
    
    webpages = AccessRecords.objects.order_by('date')
    mydict = {'wpages':webpages}
    return render(request,"app1/index.html",mydict)
