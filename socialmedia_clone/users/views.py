from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:   
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def my_logout(request):
    logger.debug(f"Request data: {request}")
    logout(request)
    messages.success(request, f'You were logged out successfully!.')
    return redirect('login')
      
@login_required
def profile(request):
     return render(request, 'users/profile.html')