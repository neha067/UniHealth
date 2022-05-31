from email import message
from multiprocessing import context
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import StudentForm
def index(request):
    
    return render(request,'index.html')
# Create your views here.

def about(request):
    return HttpResponse("this is about....")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1) #inbuilt function
        if user is not None:
            login(request,user)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/app/index')
    return render(request, 'signin.html') #context is sent to html doc....

def signup(request):
    if request.method =="POST":
        username= request.POST['username']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        #applying constraints error... doesn't work :3
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/app/index')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/app/index')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/app/index')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/app/index')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/app/index')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request,"Your account has been successfully created!")

        return redirect('signin')
    return render(request, 'signup.html') 

def addStudent(request):
    
    # if request.method =="POST":
    #     studentName= request.POST['name']
    #     regNo = request.POST['regNo']
    #     email= request.POST['email']
    #     phone= request.POST['phone']
    #     address= request.POST['address']
    #     age= request.POST['age']
    #     gender = request.POST['gender']
    #     dob = request.POST['dob']
    if request.method =="POST":
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,'addStudent.html')
    else:
        return render(request,'addStudent.html')
