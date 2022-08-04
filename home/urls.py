from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [    #URL dispatching.....
    path('', views.index, name='index'),  #calls the index function from view
    path('index',views.index, name= 'index'),  #calls about function from view
    path('signin',views.signin, name= 'signin'),
    # path('getdata/data/$',views.get_data, name= 'get_data'),
    path('signup',views.signup, name= 'signup'),
    path('addStudent',views.addStudent, name= 'addStudent'),
    path('addDoctor',views.addDoctor, name= 'addDoctor'),
    path('allStudent',views.allStudent, name= 'allStudent'),
    path('allDoctor',views.allDoctor, name= 'allDoctor'),
    
    # all doctor index
    #path('index',views.allDoctorIndex, name= 'allDoctorIndex'),
# hhhh
    path('editStudent',views.editStudent, name= 'editStudent'),
    path('deleteStudent/<int:d_id>',views.deleteStudent, name= 'deleteStudent'),
    path('deleteDoctor/<int:d_id>',views.deleteDoctor, name= 'deleteDoctor'),
    path('updateStudent/<int:regNo>',views.updateStudent, name= 'updateStudent'),
    path('updateStudent/updaterecord/<int:regNo>', views.updaterecord, name='updaterecord'),
    path('updateDoctor/<int:d_id>',views.updateDoctor, name= 'updateDoctor'),
    path('updateDoctor/updateDrecord/<int:d_id>', views.updateDrecord, name='updateDrecord'),
]