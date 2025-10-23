from django.shortcuts import render
from django.views.generic import ListView,DetailView, TemplateView
# Create your views here.
class Home(TemplateView):
    template_name='home/index.html'