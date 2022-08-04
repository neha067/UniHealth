from email import message
from multiprocessing import context
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse
from .forms import StudentForm,DoctorForm
from .models import DoctorDetails, StudentDetails,Survey
from django.template import loader
def index(request):
    c = StudentDetails.objects.all().count() #only student count works, appointment table isn't functional for now .
    student = StudentDetails.objects.all()
    all_doc_index = DoctorDetails.objects.all
    return render(request,'index.html',{'s_count':c,'allIndex' : all_doc_index,'student' : student})
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
            messages.success(request,'Doctor added successfully !')
        else:
            messages.error(request,'Enter valid details !')
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

# for index all doctors
# def allDoctorIndex(request):
#     all_doc_index = DoctorDetails.objects.all
#     return render(request,'index.html',{'allIndex' : all_doc_index})

def deleteStudent(request,regNo):
    member = StudentDetails.objects.get(regNo=regNo)
    member.delete()
    return render(request,'allStudent.html')

def deleteDoctor(request,d_id):
    member = DoctorDetails.objects.get(d_id=d_id)
    member.delete()
    return render(request,'allDoctor.html')


def updateStudent(request,regNo):
    member = StudentDetails.objects.get(regNo=regNo)
    # template = loader.get_template('updateStudent.html')
    # context = {
    #     'mymember': member,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request,'updateStudent.html',{'mymember':member})


def updateDoctor(request,d_id):
    member = DoctorDetails.objects.get(d_id=d_id)
    # template = loader.get_template('updateStudent.html')
    # context = {
    #     'mymember': member,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request,'updateDoctor.html',{'mymember':member})


def updaterecord(request, regNo):
    s_name = request.POST['s_name']
    s_phone = request.POST['s_phone']
    sregNo = request.POST['regNo']
    address = request.POST['address']
    age = request.POST['age']
    gender = request.POST['gender']
    dob = request.POST['dob']
    address = request.POST['address']
    member = StudentDetails.objects.get(regNo=regNo)
    member.s_name = s_name
    member.s_phone = s_phone
    member.regNo = sregNo
    member.address = address
    member.age = age
    member.gender = gender
    member.dob = dob
    member.save()
    return HttpResponseRedirect(reverse('allStudent'))

def updateDrecord(request, d_id):
    d_name = request.POST['d_name']
    phone = request.POST['phone']
    d_id = request.POST['d_id']
    specialization = request.POST['specialization']
    age = request.POST['age']
    gender = request.POST['gender']
    experience = request.POST['experience']
    email = request.POST['email']
    available = request.POST['available']
    member = DoctorDetails.objects.get(d_id=d_id)
    member.d_name = d_name
    member.d_id = d_id
    member.phone = phone
    member.age = age
    member.email = email
    member.gender = gender
    member.specialization = specialization
    member.experience = experience
    member.available = available    
    member.save()
    return HttpResponseRedirect(reverse('allDoctor'))
