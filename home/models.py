from operator import mod
from tkinter import CASCADE, PROJECTING
from django.db import models

class StudentDetails(models.Model):
    regNo = models.IntegerField(unique = True)
    s_name = models.CharField(max_length=20)
    s_phone = models.IntegerField()
    s_email = models.EmailField()
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
    regNo = models.IntegerField()
    docNameSpec = models.CharField(max_length=200)
    appDate = models.DateField()
    timeSlot = models.CharField(max_length=20)
    tokenNo = models.IntegerField(primary_key=True)
    problem = models.CharField(max_length=200)
