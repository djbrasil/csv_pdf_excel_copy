from django.db.models import Q
from django.shortcuts import render,redirect
from .models import * 
from django.contrib import messages 
import random 

def Index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
 
def add_category(request): 
    error = ""
    if request.method=="POST":
        cn = request.POST['categoryname']
        try:
            Category.objects.create(categoryname=cn)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_category.html', d)

def manage_category(request): 
    category = Category.objects.all()
    d = {'category':category}
    return render(request, 'manage_category.html', d)
 
def delete_category(request,pid): 
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('manage_category')

def edit_category(request,pid): 
    category = Category.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        cn = request.POST['categoryname']
        category.categoryname = cn
        try:
            category.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category}
    return render(request, 'edit_category.html',d) 