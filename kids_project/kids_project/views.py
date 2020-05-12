from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home_page(request):
    return render (request,"welcome.html")

def about(request):
    return render (request,"about.html")
