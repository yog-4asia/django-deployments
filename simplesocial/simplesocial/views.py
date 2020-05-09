from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class TestPage (TemplateView):
    template_name = "test.html"

class ThanksPage (TemplateView):
    template_name = "thanks.html"

class HomePage (TemplateView):
    template_name = "index.html"
