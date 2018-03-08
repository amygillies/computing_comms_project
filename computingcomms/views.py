# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'computingcomms/home.html', {})

def about(request):
    return HttpResponse("Computing Comms - About")

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

def about(request):
    return HttpResponse("Computing Comms - About Us")

def contact(request):
    return HttpResponse("Computing Comms - Contact Us")

def faq(request):
    return HttpResponse("Computing Comms - Frequently Asked Questions")

def user_login(request):
    return HttpResponse("Computing Comms - Login")

def my_account(request):
    return HttpResponse("Computing Comms - My Account")

def register(request):
    return HttpResponse("Computing Comms - Register")

def my_questions(request):
    return HttpResponse("Computing Comms - My Questions")

def my_comments(request):
    return HttpResponse("Computing Comms - My Comments")
