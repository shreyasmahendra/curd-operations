from json import JSONDecodeError

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from register.models import User
import json
import jwt

# Create your views here.
def login(request):
    print('login')
    context ={

    }
    return render(request , 'login/index.html', context)


def operations(request):
    print(request.content_type)
    if request.content_type == 'application/json':
        # use the below code, to read the body when the Content-Type is application/json
        print(request.body)
        # Get/fetch/return the HTTP Request Body.
        body = request.body
        # decodes or convert from binary to utf . encoding
        body = body.decode('utf-8')
        # Loads the Python Objects from string.
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return HttpResponse("invalid details", status=400)

        # Access the python data structure
        if 'email' not in body:
            return HttpResponse("please enter the email address", status=400)
        if 'password' not in body:
            return HttpResponse("please enter password", status=400)
        email = body['email']
        password = body['password']
    else:
        if 'email' not in request.POST:
            return HttpResponse("please enter the email address", status=400)
        if 'password' not in request.POST:
            return HttpResponse("please enter password", status=400)
        email = request.POST['email']
        password = request.POST['password']

    u = User.objects.filter(email=email,password=password)
    if u.exists():
        payload_data = {
            'id': u[0].id,
            'email': u[0].email,
            'name': u[0].name,
        }

        token = jwt.encode(payload=payload_data, key ='secret', algorithm="HS256")
        print(token)
        response = {
            'token' : token
        }
        return HttpResponse(json.dumps(response) ,status=200)
    else:
        if request.method != 'POST':
            return HttpResponse("method not allowed", status=405)
        else:
            return HttpResponseRedirect(reverse('login-page'))


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login-page'))
