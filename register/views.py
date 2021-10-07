from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import json
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .form import *
# Create your views here.
def register(request):
    context ={

    }
    return render(request,'register/home.html', context)

def add(request):
    if request.method != 'POST':
        return HttpResponse("Method not allowed" , status=405)
    
    print(request.content_type)
    if request.content_type == 'application/json':
        #use the below code, to ready when the content-type is an application/json
        print(request.body)
        #get/fetch/return the Http Request Body.
        body = request.body
        #it will decode and convert into binary to utf.
        body = body.decode('utf-8')
        #loads the object from utf string.
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return HttpResponse("invalid detail",status=400)
            
        #Access the python data
        if 'name' not in body:
            return HttpResponse("please enter the name",status=400)
        if 'email' not in body:
            return HttpResponse("please enter the email", status=400)
        if 'password' not in body:
            return HttpResponse("please enter the password", status=400)
        name = body['name']
        email = body['email']
        password = body['password']
    else:
        
        if 'name' not in request.POST:
            return HttpResponse("please enter name", status=400)
        if 'email' not in request.POST:
            return HttpResponse("please enter email", status=400)
        if 'password' not in request.POST:
            return HttpResponse("please enter password", status=400)
        submitted_form = UploadImageForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
        else:
            alert_message = {
                'status': False,
                'message': 'Form data is invalid. Please check if your images / title is repeated'
            }

        form = UploadImageForm()
        context = {
            'form': form,
            'images': User.objects.all
        }
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
       
    if User.objects.filter(email=email).exists():
        return HttpResponse( email+" already exist", status=409)
    
    User(name=name,email=email,password=password).save()
    return HttpResponse(request, context)



def index(request):
    if request.method == 'POST':
        submitted_form = UploadImageForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            submitted_form.save()
        else:
            alert_message = {
                'status': False,
                'message': 'Form data is invalid. Please check if your images / title is repeated'
            }

    form = UploadImageForm()
    context = {
        'form': form,
        'images': User.objects.all
    }
    return HttpResponse(request, context)


