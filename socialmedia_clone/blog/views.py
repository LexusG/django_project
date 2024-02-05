from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
# This function handles the traffic from the blog's homepage 

def about(request):
    return HttpResponse('<h1> About Page</h1>')
# This function handles the traffic from the blog's about page