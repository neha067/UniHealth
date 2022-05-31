from dataclasses import field
from django.forms import ModelForm
# from django import forms
from .models import StudentDetails, DoctorDetails

class StudentForm(ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['regNo','s_name','s_phone','s_email','address','age','gender','dob']

class DoctorForm(ModelForm):
    class Meta:
        model=DoctorDetails
        field=['d_id','d_name','specialization','experience','email','phone','gender','age']