from django.contrib import admin
from .models import StudentDetails,DoctorDetails
# Register your models here.

admin.site.register(StudentDetails)
admin.site.register(DoctorDetails)
