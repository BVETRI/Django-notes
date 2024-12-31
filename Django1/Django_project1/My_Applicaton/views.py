from django.shortcuts import render
from django.http import HttpResponse
import os



# Create your views here.
def home(request):
    return render(request,'Index.html')

def register(request):
    name=request.post["Name"]
    password=request.post["Password"]
    address=request.post["Address"]
    mail=request.post["Mail"]
    
    return render(request,"output.html",{'Name:name','password:password','Address:address','Mail:mail'})