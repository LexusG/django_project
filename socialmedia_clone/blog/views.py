from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')
# This function handles the traffic from the blog's homepage 

def about(request):
    return render(request, 'blog/about.html')
# This function handles the traffic from the blog's about page