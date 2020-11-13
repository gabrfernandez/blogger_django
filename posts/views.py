from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here, class based views
class IndexView(TemplateView):
    template_name = "posts/index.html"