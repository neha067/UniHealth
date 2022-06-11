from dataclasses import field, fields
from django.forms import ModelForm
# from django import forms
from .models import Appointment, StudentDetails,DoctorDetails
# , specialist, availableDocs

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
        fields=['regNo','deptName','docName','appDate','timeSlot','tokenNo','problem']
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['docName'].queryset = DoctorDetails.objects.none() #for dynamic field