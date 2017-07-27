from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone    
from django.db.models import Q
from .models import imager
from django.urls import reverse
import json
from django.db import connection

def Signup(request):

    request.session['signerror']="false"
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        print username
        if not username or not email or not password or not confirmpassword:
            request.session['signerror']="true"
            request.session['serrormessage']="All fields required"
        elif User.objects.filter(username=username).exists():
            request.session['signerror']="true"
            request.session['serrormessage']="Username already exist"
        elif not password == confirmpassword:
            request.session['signerror']="true"
            request.session['serrormessage']="Password do not match"
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            member=imager.objects.create(user=user)
            request.session['signerror']="false"
            return redirect('/home/')
    return render(request,'uploader/signup.html')

    


def Login(request):
    request.session['logerror']="false"
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            request.session['logerror']="false"
            return redirect('/home/')
        else:
            request.session['logerror']="true"
            request.session['lerrormessage'] = "Invalid credentials"
            
    return render(request,'uploader/login.html')                            

def Logout(request):
    logout(request)
    return redirect('/')

def home(request):
    all_file=imager.objects.all()
    print all_file

    return render(request,'uploader/album.html',{'all_file':all_file})

def upload(request):
    if request.method=='POST':
        pic=request.FILES.get('filename')

        description=request.POST.get('description')
        print pic
        print description
        if not pic or not description:
            print ">>>>>>>>>>>>>>>>"
            return redirect('home')
        upload_file = imager.objects.create(user=request.user,image=pic,description=description)
        return redirect('home')        
        