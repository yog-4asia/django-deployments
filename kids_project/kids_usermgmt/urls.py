from kids_usermgmt import urls
from kids_quiz import urls
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib import admin
from django.urls import path, include
from kids_tutorial import urls

app_name = 'kids_usermgmt'
urlpatterns = [
    path('user/register',views.register,name='register'),
    path('user/login',views.user_login,name='user_login'),
    path('user/logout',views.user_logout,name='user_logout'),

]
