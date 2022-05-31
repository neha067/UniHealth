from django.db import models
from django.forms import DateField
# Create your models here.

# class Student(models.Model):
#     student_id = models.AutoField #IntegerField that automatically increments according to available IDs
#     student_name = models.CharField(max_length=20)
#     email = models.CharField(max_length=40)
    
#     regNo = models.IntegerField(unique = True)
#     phone= models.IntegerField()
#     address = models.CharField(max_length=150)
#     age = models.IntegerField()
#     gender = models.CharField (max_length=10)
#     dob = models.DateField() 

class StudentDetails(models.Model):
    regNo = models.IntegerField(unique = True)
    s_name = models.CharField(max_length=20)
    s_phone = models.IntegerField()
    s_email = models.EmailField()
    # s_email = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField( max_length=2)
    dob = models.DateField()




