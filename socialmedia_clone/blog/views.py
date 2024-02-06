from django.shortcuts import render

posts = [
    {
        'author': 'Porkman',
        'title':  'Blog 1',
        'content': 'Ass is phat',
        'date_posted': 'August 10, 2034'
    },
    
    {
        'author': 'Thoran',
        'title':  'Blog 2',
        'content': 'Lighting of a God',
        'date_posted': 'June 10, 1287'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
# This function handles the traffic from the blog's homepage 

def about(request):
    return render(request, 'blog/about.html')
# This function handles the traffic from the blog's about page