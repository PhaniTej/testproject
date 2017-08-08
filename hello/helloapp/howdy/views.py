from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"