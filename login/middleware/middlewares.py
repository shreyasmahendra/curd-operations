from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.shortcuts import render
from register.models import User
import jwt
import json


def my_middleware(get_response):
    def home(request):
        if 'login'not in request.path and 'register' not in request.path:
            if 'Authorization' not in request.headers:
                return HttpResponse("please login" ,status=401)
        print('MIddleware called')
        if 'Authorization' in request.headers:
            print('Auth')
            token = request.headers['Authorization']
            b = jwt.decode(token,key='secret', algorithms="HS256")
            request.user = b
            print(request.user)
            a = request.user
            user_id = a['id']
            request.user_id = user_id
            print(request.user_id)
            if not User.objects.filter(id=b['id']).exists():
                #u= User.objects.filter(id=b['id'])
                
                print('Login redirect')
                return HttpResponseRedirect(reverse('login-page'))
                
        response = get_response(request)
        print('login sucessfull')
        return response
    return home
