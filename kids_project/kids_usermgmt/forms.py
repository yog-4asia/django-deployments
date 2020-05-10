from django import forms
from django.contrib.auth.models import User
from kids_usermgmt.models import UserProfileInfo
from . import models

class UserForm(forms.ModelForm):
    password = forms.CharField (widget=forms.PasswordInput(attrs={'class' : 'passwordfieldclass'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'registerfieldclass'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'registerfieldclass'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'registerfieldclass'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'emailfieldclass'}))
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.URLField (widget=forms.URLInput(attrs={'class' : 'profile_sitefieldclass'}))
    # profile_pic = forms.ImageField (widget=forms.URLInput(attrs={'class' : 'registerfieldclass'}))
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
