from django.shortcuts import render,HttpResponseRedirect
from . import forms
from .models import Car
# Create your views here.

def index(request):
    return render(request,'crudapp/base.html')

def AddSearchCar(request):
    # fi = forms.CarForm()
    if request.method == "POST":
        fi = forms.CarForm(request.POST)
        if fi.is_valid():
            name = fi.cleaned_data['name']
            color = fi.cleaned_data['color']
            car_number = fi.cleaned_data['car_number']
            reg_city = fi.cleaned_data['reg_city']
            ci = Car(name=name,color=color,car_number=car_number,reg_city=reg_city)
            ci.save()
            fi = forms.CarForm()
    else:
        fi = forms.CarForm()
    ci = Car.objects.all()
    return render(request, 'crudapp/AddSearchCar.html', context={'form': fi, 'cars':ci})

def DeleteCar(request,id):
    if request.method == 'POST':
        ci= Car.objects.get(pk=id)
        ci.delete()
    return HttpResponseRedirect("/")

def UpdateCar(request, id):

    if request.method == 'POST':
        ci = Car.objects.get(pk=id)
        fi = forms.CarForm(request.POST, instance=ci)
        fi.save()
        return HttpResponseRedirect("/")

    ci = Car.objects.get(pk=id)
    fm = forms.CarForm(instance=ci)

    return render(request,'crudapp/UpdateCar.html',context={'form':fm})



