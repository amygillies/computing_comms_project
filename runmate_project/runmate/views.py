# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'runmate/index.html', {})

def dataView(request):
    return render(request, 'runmate/loadedData.html', {})
