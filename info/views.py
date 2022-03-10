from django.shortcuts import render
from register.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
import json
from .models import Product
import jwt

# Create your views here.

def operation(request):
    if request.method != 'GET':
        return HttpResponse("method not allowed",status=405)
        
    a = []
    for user in User.objects.all():
        a.append({
            'name':user.name,
            'email':user.email,
            'password':user.password
        })
    return HttpResponse(json.dumps(a),content_type="application/json")    
        
    

def edit(request, user_id):
    if request.method != 'GET':
        return HttpResponse("Method not allowed", status=405)
    y = User.objects.filter(id=user_id)
    context ={
        'user': y[0]
    }
    print(y[0])
    return render(request, 'info/edit.html', context)

def update(request,user_id ):
    if request.method =='PUT':
        return HttpResponse(status=200)
        print(request.content_type)
        if request.content_type == 'application/json':
            print(request.body)
            # get/fetch/return the Http Request Body.
            body = request.body
            # it will decode and convert into binary to utf.
            body = body.decode('utf-8')
            # loads the object from utf string.
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                return HttpResponse("not found", status=404)

            # Access the python data
            if 'name' not in body:
                return HttpResponse("please enter the name", status=400)
            if 'email' not in body:
                return HttpResponse("please enter the email", status=400)
            if 'password' not in body:
                return HttpResponse("please enter the password", status=400)
            name = body['name']
            email = body['email']
            password = body['password']
            u = User.objects.filter(id=user_id)
            if u.exists():
                u.update(name=name,email=email,password=password)
                return HttpResponse("updated", status=200)
            else:
                User(id=user_id,name=name,email=email,password=password).save()
                return HttpResponse("id inserted ", status=201)
        else:
            return HttpResponse("not a json datatype", status=404)
    else:
        if request.method == 'PATCH':
            print(request.content_type)
            if request.content_type == 'application/json':
                body = request.body
                body = body.decode('utf-8')
            try:    
                body = json.loads(body)
            except json.JSONDecodeError:
                return HttpResponse("not found", status=404)
        if  'name' in body:
            name = body['name']
            User.objects.filter(id=user_id).update(name=name)
            return HttpResponse("name updated",status=201)
        elif 'email' in body:
            email = body['email']
            User.objects.filter(id=user_id).update(email=email)
            return HttpResponse("email updated",status=201)
        else:
            password = body['password']
            User.objects.filter(id=user_id).update(password=password)
            return HttpResponse("password updated",status=201)
                
    return HttpResponse("sucess",status=200)            
                
         
            
   


def delete(request, user_id):
    if request.method != 'DELETE':
        return HttpResponse("Method not allowed", status=405)
    u = User.objects.filter(id=user_id)
    u.delete()
    return HttpResponse(status=204)

def product(request):
    if request.method != 'GET':
        return HttpResponse("Method not allowed", status=405)
    context = {

        }
    return render(request, 'info/product.html', context)


def productList(request):
    print('List coming here')
    if request.method != 'POST':
        return HttpResponse("Method not allowed", status=405) 
    if request.content_type == 'application/json':
        print(request.body)
        body = request.body
        body = body.decode('utf-8')
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return HttpResponse("invalid detail",status=400)

        if 'product_name' not in body:
            return HttpResponse("please enter the product_name", status=400)
        if 'product_price' not in body:
            return HttpResponse("please enter the product_price", status=400)
        product_name = body['product_name']
        product_price = body['product_price']

    else:

        #if 'Authorization' in request.headers:
            #token = request.headers['Authorization']
           #b = jwt.decode(token, key='secret', algorithms="HS256")
            #print(b['id'])
            
            if 'product_name' not in request.POST:
                return HttpResponse("please enter product_name", status=400)
            if 'product_price' not in request.POST:
                return HttpResponse("please enter product_price", status=400)
            
            product_name = request.POST['product_name']
            product_price = request.POST['product_price']
          
    Product(product_name = product_name,product_price = product_price, user_id_id = request.user_id ).save() 
    return HttpResponse("sucess",status=200)

def pedit(request):
    if request.method != 'GET':
        return HttpResponse("method not allowed",status=405)
        
    u = User.objects.get(id= request.user_id)     
    response = {"name":[],"product":[],"productcount":[]}
    response["name"] = u.name
    a = []   
    for user in Product.objects.filter(user_id_id = request.user_id):
        a.append({
                    'id':user.id,
                    'product_name':user.product_name,
                    'product_price':user.product_price,
       
               })
    response["productcount"]= len(a)
    response["product"]= a
    return HttpResponse(json.dumps(response),content_type="application/json")
    
def getproduct(request,p_id):
    if request.method != 'GET':
        return HttpResponse("Method not allowed", status=405)
    a =[]    
    for user in Product.objects.filter(id=p_id):
        a.append({
                    'id':user.id,
                    'product_name':user.product_name,
                    'product_price':user.product_price,
            })
    return HttpResponse(json.dumps(a),content_type="application/json")
    
    

def productupdate(request):
    if request.method != 'PUT':
        return HttpResponse("Method not allowed", status=405)
    
        #json body loading
    if request.content_type == 'application/json':
        #print(request.body)
        body = request.body
        body = body.decode('utf-8')
        print(body)
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return HttpResponse("invalid detail",status=400)
        if type(body) is dict:
            body =[body]
            print(body)
            #if 'product_name' not in body:
                #return HttpResponse("please enter the product_name", status=400)
            #if 'product_price' not in body:
                #return HttpResponse("please enter the product_price", status=400)
        for i in body:
            p_id  = i['id']
            product_name = i['product_name']
            product_price = i['product_price']
            u = Product.objects.filter(user_id_id= request.user_id,id = p_id)
            if u.exists():
                u.update(product_name = product_name,product_price =product_price)
                
            else:
                Product(product_name = product_name,product_price = product_price, user_id_id = request.user_id ).save()   
        return  HttpResponse("success")  
        
    return HttpResponse("sucess",status=200)
    
    
def productdelete(request,p_id):
    if request.method != 'DELETE':
        return HttpResponse("Method not allowed", status=405)
        Product.objects.filter(user_id_id=request.user_id ,id = p_id).delete()
    return HttpResponse(status=204)
   