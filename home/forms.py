from dataclasses import field
from django.forms import ModelForm
# from django import forms
from .models import StudentDetails

class StudentForm(ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['regNo','s_name','s_phone','s_email','address','age','gender','dob']