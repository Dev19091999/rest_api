from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.

class lista(APIView):
   def get(self,request,id):
      employees_data=employees.objects.get(id = id)
      serializer=employeesSerializer(employees_data)
      return Response(serializer.data)

class listb(APIView): 
   def get(self,request):    
       employees_data=employees.objects.all()
       serializer=employeesSerializer(employees_data,many=True)
       return Response(serializer.data)
      
      
   def post(self,request):
      if request.data.get("id",None):
         rem=employees.objects.get(id=request.data.get("id"))
         rem.delete()
         return Response({"Particular_Data":"Deleted"})
      take=request.data
      employees.objects.create(firstname=take['firstname'],lastname=take['lastname'],contact=take['contact'],emp_id=take['emp_id'])
      return Response({'Status':'Successfully Done'})
      
      
   
   def delete(self,request):
      employees.objects.all().delete()
      return Response({'Status':'Deleted Successfully'})
      
      
   def put(self,request):
      req_data = request.data
      upd = employeesSerializer(employees.objects.get(id=req_data["id"]),req_data)
      if upd.is_valid():
         upd.save()
         return Response({"Updated":"Successfully"})
      else:
         print(post)
         return Response({"Data":"Not Found"})
     
     
   
