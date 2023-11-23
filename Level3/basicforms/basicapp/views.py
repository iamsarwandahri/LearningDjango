from django.shortcuts import render
from basicapp.formpage import FormName

def index(request):
    return render(request,'basicapp/index.html',{'Name':'Sarwan'})

def formindex(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Name "+form.cleaned_data['name'])
            print('Email '+form.cleaned_data['email'])
            print('Vemail '+form.cleaned_data['vemail'])
            print('Text '+form.cleaned_data['text'])

    return render(request,'basicapp/form_page.html',{'form':form})
