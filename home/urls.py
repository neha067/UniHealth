from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [    #URL dispatching.....
    path('', views.index, name='index'),  #calls the index function from view
    path('index',views.index, name= 'index'),  #calls about function from view
    path('signin',views.signin, name= 'signin'),
    path('signup',views.signup, name= 'signup'),
    path('addStudent',views.addStudent, name= 'addStudent'),
    path('addDoctor',views.addDoctor, name= 'addDoctor'),
    path('editStudent',views.editStudent, name= 'editStudent')
]