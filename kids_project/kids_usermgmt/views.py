from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def register(request):

    return render(request,"register.html")

def user_login(request):

    return render(request,"login.html")

def user_logout(request):

    return render(request,"logout.html")
