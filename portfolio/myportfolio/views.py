import re
from datetime import datetime
import bleach
from django.http import HttpResponse
from  django.contrib import messages
# from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import About

# Create your views here.

def home(request):
    return render (request, 'myportfolio/index.html')

def about(request):
    msg = messages.get_messages(request)
    allData = About.objects.all()
    data = {'key': allData, 'msg': msg}
    return render (request, 'admin/about.html', data)

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
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z.]+\.[a-zA-Z]$"

    # Check if any of the required fields is empty
    if not all([u_name, dob, phone, email, no_exp, no_happy_customers, no_project_finished, no_digital_awards, description]):
        messages.success(request, "The field cnnot be empty!")
        # return HttpResponse("All fields are required")
    
    if not re.match(pattern, email):
        messages.success(request, "your email ID is not supported!")
    else:
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


def about_edit(request, id):
    editable = About.objects.get(id = id)
    editdata = {'d': editable}
    return render (request, 'admin/edit.html', editdata)

def edited(request):
    id = request.POST.get('id')
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


    about_obj = About.objects.get(id = id)

    about_obj.u_name = u_name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = no_exp
    about_obj.no_happy_customers = no_happy_customers
    about_obj.no_project_finished = no_project_finished
    about_obj.no_digital_awards = no_digital_awards
    about_obj.description = description
    # about_obj.date_time = formatted_datetime

    about_obj.save()

    return redirect('about')

    # return render (request, 'admin/about.html')


def delete(request, id):
    deleteable = About.objects.get(id = id)
    deleteable.delete()
    return redirect('about')