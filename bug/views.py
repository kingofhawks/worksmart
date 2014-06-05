from django.shortcuts import render

# Create your views here.
#-*- coding: UTF-8 -*-

# Create your views here.
from django.shortcuts import render
from django.utils import simplejson
from django.http import HttpResponse
from django.http import Http404
import json
from models import BugStatistics
import bson
from bson import json_util


def trend(request):
    return render(request,'trend.html')

def trend_data(request):
    from django.core import serializers
    query_set = BugStatistics.objects.all()
    #data = serializers.serialize("json", query_set)
    bugs = []
    for bug in query_set:
        #print bug
        #print type(bug)
        bugs.append({'x':bug.date,'y':bug.total})
    print bugs
    #json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder
    data = [ { 'x': -1893456000, 'y': 92228531 }, { 'x': -1577923200, 'y': 106021568 } ];
    from django.core.serializers.json import DjangoJSONEncoder
    return HttpResponse(json.dumps(bugs, cls=DjangoJSONEncoder), mimetype="application/json")






