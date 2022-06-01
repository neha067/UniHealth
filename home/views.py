from email import message
from multiprocessing import context
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse
from .forms import StudentForm,DoctorForm
from .models import DoctorDetails, StudentDetails
def index(request):
    
    return render(request,'index.html')
# Create your views here.

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
            return redirect('/app/signin')
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
            return redirect('/app/signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/app/signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/app/signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/app/signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('/app/signup')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request,"Your account has been successfully created!")

        return redirect('/app/signup')
    return render(request, 'signup.html') 

def addStudent(request):
    if request.method =="POST":
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Student added successfully !')
        else:     
            messages.error(request,'Enter valid details !')
        return render(request,'addStudent.html')
    else:
        return render(request,'addStudent.html')

def addDoctor(request):
    if request.method =="POST":
        form = DoctorForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,'addDoctor.html')
    else:
        return render(request,'addDoctor.html')

def editStudent(request):
    return render(request,'editStudent.html')

def allStudent(request):
    all_student = StudentDetails.objects.all
    return render(request,'allStudent.html',{'all' : all_student})

def allDoctor(request):
    all_doc = DoctorDetails.objects.all
    return render(request,'allDoctor.html',{'all' : all_doc})

def deleteStudent(request,regNo):
    member = StudentDetails.objects.get(regNo=regNo)
    member.delete()
    return render(request,'allStudent.html')


def deleteDoctor(request,d_id):
    member = DoctorDetails.objects.get(d_id=d_id)
    member.delete()
    return render(request,'allDoctor.html')

