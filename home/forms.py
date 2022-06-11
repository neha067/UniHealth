from dataclasses import field, fields
from django.forms import ModelForm
from django import forms
from .models import Appointment, StudentDetails,DoctorDetails
class StudentForm(ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['regNo','s_name','s_phone','s_email','address','age','gender','dob']

class DoctorForm(ModelForm):
    class Meta:
        model=DoctorDetails
        fields=['d_id','d_name','specialization','experience','email','phone','gender','age']

class AppointmentForm(ModelForm):
    class Meta:
        model =  Appointment
        fields=['regNo','appDate','docNameSpec','timeSlot','tokenNo','problem']