"""
URL configuration for socialmedia_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
import logging
from django.conf import settings
from django.conf.urls.static import static

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def my_view(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    # Your view logic here
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register',),
    path('profile/', user_views.profile, name='profile',),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',), name='login'),
    path('logout/', user_views.my_logout, name='logout'),
    path('', include('blog.urls')),
    path('my-view/', my_view, name='my-view'),
    

] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

