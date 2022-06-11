from operator import mod
from tkinter import CASCADE, PROJECTING
from django.db import models

class StudentDetails(models.Model):
    regNo = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=20)
    s_phone = models.IntegerField()
    s_email = models.EmailField()
    # s_email = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField( max_length=10)
    dob = models.DateField(blank=True, null=True)
    # class Meta:
    #     abstract = True

class DoctorDetails(models.Model):
    d_id=models.IntegerField(primary_key=True)
    d_name=models.CharField(max_length=20, null=False)
    specialization=models.CharField(max_length=40,null=False)
    experience=models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField( max_length=10)
    age = models.IntegerField()
<<<<<<< HEAD
<<<<<<< HEAD
=======
    # class Meta:
    #     abstract = True

class Appointment(models.Model):
    regNo = models.IntegerField()
    deptName = models.ForeignKey(DoctorDetails, on_delete=models.SET_NULL, null=True, related_name='deptName')
    # deptName = models.CharField(max_length=20)
    docName = models.ForeignKey(DoctorDetails,on_delete=models.SET_NULL, null=True,related_name='docName')
    # dName = availableDocs.dName
    # sName = availableDocs.sName
    appDate = models.DateField(blank=True, null=True)
    timeSlot = models.CharField(max_length=20)
    tokenNo = models.AutoField(primary_key=True)
    problem = models.CharField(max_length=200)
    

# class Department(models.Model):
#     deptName = models.CharField(primary_key=True)
#     class Meta:
#         db_table = "specialization"

# class DoctorNames(models.Model):
#     docName = models.CharField()
# class specialist(models.Model):
#     sName = models.CharField(primary_key=True,max_length=40)
#     class Meta:
#         db_table = "specialization"

# class availableDocs(models.Model):
#     dName = models.CharField(null=False, max_length=20)
#     sName = models.CharField(max_length=40)
#     class Meta:
#         db_table = "home_doctordetails"
#         managed = False #This allowed me to use home_doctordetails here otherwise it can't be used
>>>>>>> test1

=======
    available = models.CharField(max_length=15, default="Available")
>>>>>>> cff06094ccb16ee6e0b1465bd60edbdbd5b84b21
