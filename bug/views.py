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
import arrow


def trend(request):
    return render(request,'trend.html')

def trend_data(request):
    from django.core import serializers
    query_set = BugStatistics.objects.all()
    #data = serializers.serialize("json", query_set)
    total_bugs = []
    closed_bugs = []
    result = []

    for bug in query_set:
        #print bug
        #total_bugs.append({'x':bug.date,'y':bug.total})
        #closed_bugs.append({'x':bug.date,'y':bug.closed}
        date_epoch = arrow.get(bug.date).timestamp
        total_bugs.append({'x':date_epoch,'y':bug.total})
        closed_bugs.append({'x':date_epoch,'y':bug.closed})
    result = [{'name':'total','color': 'lightblue','data':total_bugs},{'name':'closed','color': 'steelblue','data':closed_bugs}]
    print result

    #json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder

    from django.core.serializers.json import DjangoJSONEncoder
    return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), mimetype="application/json")

def percentage(request):
    return render(request,'percentage.html')

def percentage_data(request):
    from django.core import serializers
    query_set = BugStatistics.objects.all()
    #data = serializers.serialize("json", query_set)
    total_bugs = []
    closed_bugs = []
    result = []

    for bug in query_set:
        #print bug
        #total_bugs.append({'x':bug.date,'y':bug.total})
        #closed_bugs.append({'x':bug.date,'y':bug.closed}
        date_epoch = arrow.get(bug.date).timestamp
        total_bugs.append({'x':date_epoch,'y':bug.total})
        closed_bugs.append({'x':date_epoch,'y':bug.closed})
    result = [{'name':'total','color': 'lightblue','data':total_bugs},{'name':'closed','color': 'steelblue','data':closed_bugs}]
    print result

    #json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder

    from django.core.serializers.json import DjangoJSONEncoder
    return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), mimetype="application/json")






