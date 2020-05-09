from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from Project_Two_App import views

urlpatterns = [

    path('',views.help,name='help'),
    path('',views.index,name='index'),
    
    #path('',views.index),

]
