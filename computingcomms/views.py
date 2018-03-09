# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from computingcomms.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'computingcomms/home.html', {})

def about(request):
    return render(request, 'computingcomms/about_us.html', {})

def quizzes(request):
    return render(request, 'computingcomms/quizzes.html', {})

def jp2(request):
    return HttpResponse("Computing Comms - Java Programming 2 Quiz")

def oose2(request):
    return HttpResponse("Computing Comms - Object Orientated Software Engineering Quiz")

def wad2(request):
    return HttpResponse("Computing Comms - Web App Development 2 Quiz")

def ads2(request):
    return HttpResponse("Computing Comms - Algorithms and Data Structures 2 Quiz")

def cs2t(request):
    return HttpResponse("Computing Comms - Computing Systems 2 Quiz")

def af2(request):
    return HttpResponse("Computing Comms - Algorithmic Foundations 2 Quiz")

def forum(request):
    return HttpResponse("Computing Comms - Forum")

def contact(request):
     return render(request, 'computingcomms/contact_us.html', {})

def faq(request):
    return render(request, 'computingcomms/faq.html', {})

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Computing Comms account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'computingcomms/login.html', {})

def my_account(request):
    return HttpResponse("Computing Comms - My Account")

def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'computingcomms/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def my_questions(request):
    return HttpResponse("Computing Comms - My Questions")

def my_comments(request):
    return HttpResponse("Computing Comms - My Comments")
