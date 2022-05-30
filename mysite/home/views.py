from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
def index(request):
    
    return render(request,'index.html')
# Create your views here.

def about(request):
    return HttpResponse("this is about....")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1) #inbuilt function
        if user is not None:
            login(request)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('app')
    return render(request, 'login.html') #context is sent to html doc....

def signup(request):
    if request.method =="POST":
        username= request.POST['username']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request,"Your account has been successfully created!")

        return redirect('login')
    return render(request, 'signup.html') 
