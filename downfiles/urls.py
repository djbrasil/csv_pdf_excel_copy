"""downfiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),    
    path('add_category',add_category,name='add_category'),
    path('manage_category',manage_category,name='manage_category'),
    path('delete_category/<int:pid>', delete_category,name='delete_category'),
    path('edit_category/<int:pid>',edit_category,name='edit_category'), 
 
]
