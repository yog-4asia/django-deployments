from django.shortcuts import render
from django.http import  HttpResponse
# import mtv_app
from mtv_app.models import User

# Create your views here.
def index(request):
    return render(request,"mtv_app/welcome.html")

def help(request):
    user_records = User.objects.order_by('first_name')
    help_dict = {'user_list': user_records}
    # print(help_dict(user_list))
    return render(request,"mtv_app/help.html",context=help_dict )
