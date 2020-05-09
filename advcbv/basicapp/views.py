from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                 ListView, DetailView,
                                 CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolList(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetails(DetailView):
    context_object_name = 'school_detail'
    model = models.School

    template_name = 'basicapp/school_detail.html'

class CreateSchoolView(CreateView):
    fields = ('name', 'principal', 'address')
    model = models.School
    template_name = 'basicapp/school_form.html'

class SchoolUpdateView (UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView (DeleteView):
    model = models.School
    success_url = reverse_lazy("basicapp:list")
