from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render (request,"welcome.html")

def about(request):
    return render (request,"about.html")

def summation(request):

    return render(request,"summation.html")

def substraction(request):

    return render(request,"subtraction.html")

def multiplication(request):

    return render(request,"multiplication.html")

def division(request):

    return render(request,"division.html")
