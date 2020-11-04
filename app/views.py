from django.shortcuts import render , redirect , get_object_or_404,redirect
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.contrib.auth.forms import   UserCreationForm 
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import  login ,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
import datetime
import random
from django.contrib import messages
from django.utils.timezone import datetime

# main homepage

def home(request):
    return render(request,'index.html')

def payments(request):
    return render(request,'payment.html')


def membership(request):
    return render(request,'')

def activities(request):
    return render(request,'')

def bushcamps(request):
    return render(request,'')

def species(request):
    return render(request,'')

def gallery(request):
    return render(request,'')

def ecoschool(request):
    return render(request,'')

def supporters(request):
    return render(request,'')

def events(request):
    return render(request,'')

def contactUs(request):
    return render(request,'')

def blog(request):
    return render(request,'')

def shop(request):
    return render(request,'')

def map(request):
    return render(request,'')





# signup page
def signup(request):
    if request.method == "POST":
        form =RegistrationForm(request.POST)
        
        if form.is_valid() :
             user = form.save()
             login(request,user)
             return redirect('Student/Enrollment')
        else:
            for mssg in form.error_messages:
                print(form.error_messages[mssg])
    form = RegistrationForm()
    args = {'form' : form }
    return render(request, 'registration/signup.html',  args) 

