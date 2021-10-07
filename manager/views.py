from django.shortcuts import render
from manager import views
import json
from .models import Department
from django.http import HttpResponse
from django.views import View

# Create your views here.
class department(View):

    def get(self, request , d_id):
        a =[]    
        for dep in Department.objects.filter(id = d_id):
            a.append({
                    'id':dep.id,
                    'department_name':dep.department_name,
                    'manager_name':dep.manager_name,
                    'mobile_number':dep.mobile_number.national_number,
                })
        return HttpResponse(json.dumps(a),content_type="application/json")
    
    def post(self,request):
        if request.content_type == 'application/json':
            body = request.body
            print(request.body)
            body = body.decode('utf-8')
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                return HttpResponse("invalid details",status = 400)
            print(body)    
            if 'department_name' not in body:
                return HttpResponse("please enter the department name", status=400)
            if 'manager_name' not in body:
                return HttpResponse("please enter the manager name", status=400)
            if 'mobile_number' not in body:
                return HttpResponse("please enter the mobile number", status=400)
                
            department_name = body['department_name']
            manager_name = body['manager_name']
            mobile_number = body['mobile_number']
            
        else:
        
            if 'department_name' not in request.POST:
                return HttpResponse("please enter the department name", status=400)
            if 'manager_name' not in request.POST:
                return HttpResponse("please enter the manager name ", status=400)
            if 'mobile_number' not in request.POST:
                return HttpResponse("please enter mobile number", status=400)
                print(request.POST)
            department_name = request.POST['department_name']
            manager_name = request.POST['manager_name']
            mobile_number = request.POST['mobile_number']
        Department(department_name=department_name,manager_name=manager_name,mobile_number=mobile_number).save()
        return HttpResponse("sucess",status=200)    
    
    def put(self,request,d_id):
        if request.content_type == 'application/json':
            body = request.body
            print(request.body)
            body = body.decode('utf-8')
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                return HttpResponse("invalid details",status = 400)
            print(body)    
            if 'department_name' not in body:
                return HttpResponse("please enter the department name", status=400)
            if 'manager_name' not in body:
                return HttpResponse("please enter the manager name", status=400)
            if 'mobile_number' not in body:
                return HttpResponse("please enter the mobile number", status=400)
                
            department_name = body['department_name']
            manager_name = body['manager_name']
            mobile_number = body['mobile_number']
            
        u = Department.objects.filter(id=d_id)
        if u.exists():
            u.update(department_name = department_name , manager_name = manager_name , mobile_number = mobile_number)
            return HttpResponse("updated", status=200)
        return HttpResponse(status=200)
        
    def patch(self,request,d_id):
        if request.content_type == 'application/json':
            body = request.body
            body = body.decode('utf-8')
            body = json.loads(body)
            if  'department_name' in body:
                department_name = body['department_name']
                Department.objects.filter(id=d_id).update(department_name = department_name)
                return HttpResponse("Department Name Updated",status=201)
            elif 'manager_name' in body:
                manager_name = body['manager_name']
                Department.objects.filter(id = d_id).update(manager_name = manager_name)
                return HttpResponse("Manager Name Updated",status=201)
            else:
                mobile_number = body['mobile_number']
                Department.objects.filter(id=d_id).update(mobile_number = mobile_number)
                return HttpResponse("Mobile number updated",status=201)
        return HttpResponse("sucess" ,status=200)

    def delete(self,request,d_id):
        u = Department.objects.filter(id=d_id)
        u.delete()
        return HttpResponse("id deleted", status=204)
