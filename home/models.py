#from lib2to3.pgen2 import token
from operator import mod
import uuid
#from tkinter import CASCADE, PROJECTING
from django.db import models

class StudentDetails(models.Model):
    regNo = models.IntegerField(unique = True)
    s_name = models.CharField(max_length=20)
    s_phone = models.IntegerField()
    s_email = models.EmailField()
    # s_email = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField( max_length=10)
    dob = models.DateField(blank=True, null=True)

class DoctorDetails(models.Model):
    d_id=models.IntegerField(unique=True)
    d_name=models.CharField(max_length=20)
    specialization=models.CharField(max_length=40)
    experience=models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField( max_length=10)
    age = models.IntegerField()
    available = models.CharField(max_length=15, default="Available")

class Appointment(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    token = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    regNo = models.IntegerField()
    #d_id = models.IntegerField()
    specialization= models.CharField(max_length=20)
    d_name= models.CharField(max_length=20)
    problem= models.CharField(max_length=100)
    report = models.CharField(max_length=50,null=True)

    


