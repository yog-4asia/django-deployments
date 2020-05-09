from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def summation(request):

    return render(request,"summation.html")

def subtraction(request):

    return render(request,"subtraction.html")

def multiplication(request):

    return render(request,"multiplication.html")

def division(request):

    return render(request,"division.html")
