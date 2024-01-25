import re
from datetime import datetime
# import bleach
from django.http import HttpResponse
from  django.contrib import messages
# from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import About
import random
from django.core.signing import Signer
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render (request, 'myportfolio/index.html')

def about(request):
    if 'userID' in request.session:
        msg = messages.get_messages(request)
        allData = About.objects.all()
        data = {'key': allData, 'msg': msg}
        return render (request, 'admin/about.html', data)
    else:
        return redirect('login')

def about_insert(request):
    u_name = request.POST.get('u_name')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    no_exp = request.POST.get('exp')
    no_happy_customers = request.POST.get('customers')
    no_project_finished = request.POST.get('projects')
    no_digital_awards = request.POST.get('awards')
    description = request.POST.get('description')
    date_time  = datetime.now( )
    formatted_datetime = date_time.strftime("%d %b %Y - %I:%M %p")
    # pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z.]+\.[a-zA-Z]{2,3}$"


    currentTime = datetime.now().strftime('%H:%M:%S')
    h, m, s = map(int, currentTime.split(':'))
    timeSeconds = str(h*3600 + m*60 + s)
    randomNumbers = random.choices('0123456789', k=4)
    randomNumber = ''.join(randomNumbers)
    verfKey = timeSeconds + randomNumber
    

    signer = Signer()
    encryptedvValue = signer.sign(verfKey).split(':')[1]
    link = f"<p>Congratulations Mr {u_name} ! For registering as a user in our portfolio system. To confirm the registration </p><a href='http://127.0.0.1:8000/email_verification/"+encryptedvValue+"' target='_blank'>please click this Activation link</a>"
    send_mail(f"Mr. {u_name} Please Confirm Your Registration - portfolio",encryptedvValue,'meduorg.in2150@gmail.com',[email], html_message=link)

    # Check if any of the required fields is empty
    if not all([u_name, dob, phone, email, no_exp, no_happy_customers, no_project_finished, no_digital_awards, description]):
        messages.success(request, "The field cnnot be empty!")
        # return HttpResponse("All fields are required")
    
    # if not re.match(pattern, email):
    #     messages.success(request, "your email ID is not supported!")
    else:
        about_obj = About()

        about_obj.u_name = u_name
        about_obj.dob = dob
        about_obj.phone = phone
        about_obj.email = email
        about_obj.password = password
        about_obj.no_exp = no_exp
        about_obj.no_happy_customers = no_happy_customers
        about_obj.no_project_finished = no_project_finished
        about_obj.no_digital_awards = no_digital_awards
        about_obj.description = description
        about_obj.date_time = formatted_datetime
        about_obj.verfKey = encryptedvValue
        about_obj.verfStatus = 0

        about_obj.save()

    return redirect('registrationConfirm')

def registrationConfirm(request):
    return render (request, 'admin/regConf.html')


def email_verification(request, id):
    verfRecord = About.objects.get(verfKey=id)
    boolVar = False
    if verfRecord.verfStatus == '0':
        boolVar = False
        verfRecord.verfStatus = 1
        verfRecord.save()
    else:
        boolVar = True        
    boolDic = {'d': boolVar}
    return render(request, 'admin/registered.html', boolDic)

def login(request):
    if 'userID' in request.session:
        return redirect('about')
    else:
        return render(request, 'login.html')
def logout(request):
    request.session.flush()
    return redirect('login')


def loginAdmin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    logData = About.objects.get(email=email)

    if (logData.password==password and logData.verfStatus=='1'):
        request.session['userID'] = logData.id
        request.session['username'] = logData.u_name
        return redirect('about')
    else:
        return redirect('login')

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