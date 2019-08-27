# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,)

from django.contrib.auth import authenticate, login

# Create your views here.


def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("Username:", username, '\n' 'Password:', password)

            user = authenticate(request,
                                username=username,
                                password=password)
            login(request, user)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'User/login.html')

def user_register(request):

    return render(request, 'User/register.html')