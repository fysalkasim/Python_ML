from django.shortcuts import render

# Create your views here. importinghttpRespons
from django.http import HttpResponse

#Creating a function

def index(request):
    return HttpResponse("Hello World")
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
