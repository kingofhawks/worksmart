from django.shortcuts import render

# Create your views here.
#-*- coding: UTF-8 -*-

# Create your views here.
from django.shortcuts import render
from django.utils import simplejson
from django.http import HttpResponse
from django.http import Http404
import json


def trend(request):
    return render(request,'trend.html')




