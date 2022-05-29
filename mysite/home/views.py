from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
def index(request):
    
    return render(request,'index.html')
# Create your views here.

def about(request):
    return HttpResponse("this is about....")

def login(request):
    
    return render(request, 'login.html') #context is sent to html doc....

def signup(request):
    if request.method =="POST":
        username= request.POST.get('user')
        email= request.POST.get('email')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2') 

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request,"Your account has been successfully created!")

        return redirect('login')
    return render(request, 'signup.html') 
