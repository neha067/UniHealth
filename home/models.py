from django.db import models
# Create your models here.

class Student(models.Model):
    student_id = models.AutoField #IntegerField that automatically increments according to available IDs
    student_name = models.CharField(max_length=20)
    email = models.EmailField
    regNo = models.IntegerField(unique = True)
    phone= models.IntegerField()
    address = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField (max_length=10)
    dob = models.DateField() 


