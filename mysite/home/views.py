from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request,'index.html')
# Create your views here.

def about(request):
    return HttpResponse("this is about....")

def login(request):
    return render(request, 'login.html') #context is sent to html doc....

def register(request):
    return render(request, 'register.html') 
