from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import About

# Create your views here.

def home(request):
    return render (request, 'myportfolio/index.html')

def about(request):
    return render (request, 'admin/about.html')

def about_insert(request):
    u_name = request.POST.get('u_name')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    no_exp = request.POST.get('exp')
    no_happy_customers = request.POST.get('customers')
    no_project_finished = request.POST.get('projects')
    no_digital_awards = request.POST.get('awards')
    description = request.POST.get('description')
    date_time  = datetime.now( )
    formatted_datetime = date_time.strftime("%d %b %Y - %I:%M %p")


    about_obj = About()

    about_obj.u_name = u_name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = no_exp
    about_obj.no_happy_customers = no_happy_customers
    about_obj.no_project_finished = no_project_finished
    about_obj.no_digital_awards = no_digital_awards
    about_obj.description = description
    about_obj.date_time = formatted_datetime

    about_obj.save()

    return redirect('about')
