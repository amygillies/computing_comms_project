# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'computingcomms/home.html', {})

def about(request):
    return render(request, 'computingcomms/about_us.html', {})

def quizzes(request):
    return render(request, 'computingcomms/quizzes.html', {})

def jp2(request):
    return render(request, 'computingcomms/jp2.html', {})

def oose2(request):
    return render(request, 'computingcomms/oose2.html', {})

def wad2(request):
    return render(request, 'computingcomms/wad2.html', {})

def ads2(request):
    return render(request, 'computingcomms/ads2.html', {})

def cs2t(request):
    return render(request, 'computingcomms/cs2t.html', {})

def af2(request):
    return render(request, 'computingcomms/af2.html', {})

def forum(request):
    return render(request, 'computingcomms/forum.html', {})

def about(request):
    return render(request, 'computingcomms/about_us.html', {})

def contact(request):
    return render(request, 'computingcomms/contact_us.html', {})

def faq(request):
    return render(request, 'computingcomms/faq.html', {})

def user_login(request):
    return HttpResponse("Computing Comms - Login")

def my_account(request):
    return HttpResponse("Computing Comms - My Account")

def register(request):
    return render(request, 'computingcomms/register.html', {})

def my_questions(request):
    return HttpResponse("Computing Comms - My Questions")

def my_comments(request):
    return HttpResponse("Computing Comms - My Comments")
