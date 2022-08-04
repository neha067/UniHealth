from django.contrib import admin
from .models import StudentDetails,DoctorDetails, Survey
# Register your models here.

admin.site.register(StudentDetails)
admin.site.register(DoctorDetails)
admin.site.register(Survey)