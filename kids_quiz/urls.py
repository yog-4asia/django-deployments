from kids_usermgmt import urls
from kids_quiz import urls
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from kids_tutorial import urls
from . import views

app_name = 'kids_quiz'

urlpatterns = [
    path('quiz',views.quiz_home,name='quiz_home'),

]
