# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.messages import error

def index(request):
    return render(request, 'friendly/index.html')

def register(request):
    valid= User.objects.validate_reg(request.POST)
    if type(valid) == list:
        for e in valid:
            messages.error(request, e)
        return redirect('/')
    request.session['user_id'] = valid.id
    return redirect ('/success')

def login(request):
    valid = User.objects.validate_login(request.POST)
    if type(valid) == list:
        for e in valid:
            messages.error(request, e)
        return redirect('/')
    request.session['user_id'] = valid.id
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError: 
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']) #getting id from db and using it to display user info and other actions depending on app built
    }
    return render(request, 'friendly/success.html', context)

def logout(request):
    request.session.clear()
    return render(request,'friendly/index.html')

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    my_friends = []
    my_friends.append(request.session['user_id'])
    for key in user.friends_with.all():
        my_friends.append(key.id)
    context = {
        'count' : User.objects.all().count(),
        'user' : user,
        'otherUsers' : User.objects.exclude(id__in=my_friends),
           }
    return render(request,'friendly/dashboard.html',context)


def add(request,friend_id):
    friend = User.objects.get(id=friend_id)
    user = User.objects.get(id=request.session['user_id'])  
    user.friends_with.add(friend)      
    return redirect('/dashboard')

def remove(request,friend_id):
    user = User.objects.get(id=request.session['user_id'])
    friend = User.objects.get(id=friend_id)
    user.friends_with.remove(friend_id)
    return redirect('/dashboard')


def show(request,user_id):
    context = {
        'user': User.objects.get(id=user_id),
    }
    return render(request,'friendly/show.html',context)