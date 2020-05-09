from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Normal Landing Page")
def help(request):
    dictionary = {'help_me':'Support Contact: 9910075160'}
    return render(request,'Project_Two/help.html',context=dictionary)

# Create your views here.
