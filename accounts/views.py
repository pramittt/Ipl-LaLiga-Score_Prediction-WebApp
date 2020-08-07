from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from imdb import IMDb
import numpy as np
import os
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
    
def back(request):
    return redirect('/')

def no_operation(request):
    messages.info(request,'You must signin')
    return render(request,'login.html')

def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['Password']

        user=auth.authenticate(username=username,password=password)

        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if(password1==password2 and password1):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Usename Taken')
                return redirect('register')
            elif (User.objects.filter(email=email).exists()):
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password2, email=email, first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Something went wrong')
            return redirect('register')

    else:
        return render(request,'register.html')

def url_clean(url):
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url

def movie_info(request):
    if(request.method=='POST'):
        name=request.POST['movie_name']
        ia = IMDb()
        movies = ia.search_movie(name)
        
        movie = ia.get_movie(movies[0].movieID)
        cover= url_clean(movie['cover url'])
        cast = movie.get('cast')
        return render(request,'movie.html', {'search':cast[:6],'name':name,'cover':cover})