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
    dob = models.DateField()




