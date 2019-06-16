from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post
# Create your views here.
'''class index(TemplateView):
	template_name = 'index.html'
'''
class index(ListView):
    model = Post
    template_name = 'index.html'