#-*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import json
from models import BugStatistics
import bson
from bson import json_util
import arrow
from django.utils.translation import ugettext as _


def trend(request):
    query_set = BugStatistics.objects.order_by('-date')[:2]
    statistics = ''
    if len(query_set) >=2:
        current = query_set[0]
        previous = query_set[1]
        statistics = '目前共发现问题总数{}个(本周新增{}个)，已解决{}(本周解决{}个)，未解决{}个（本周增加{}个）'\
            .format(current.total,(current.total-previous.total),current.closed,(current.closed-previous.closed),current.open,(current.open-previous.open))
        print statistics

    msg = _('message')
    print msg

    return render(request,'trend.html',{'statistics':statistics})

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
    return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), content_type="application/json")

def percentage(request):
    from redmine import get_bugs
    bug = get_bugs()
    from models import BugStatistics
    b = BugStatistics()
    b.closed = bug['closed']
    b.open = bug['open']
    b.total = bug['total']
    b.date = bug['date']
    print b
    b.save()

    return render(request,'percentage.html')

def percentage_data(request):
    from django.core import serializers
    query_set = BugStatistics.objects.all()
    #data = serializers.serialize("json", query_set)
    percentage = []
    result = []

    for bug in query_set:
        percent = float(bug.closed)/bug.total
        percentage.append({'date':bug.date.date(),'close': '{:.2f}'.format(percent)})
    result = [{'name':'percentage','color': 'steelblue','data':percentage}]
    print result

    #json.dumps do not work with DateTime object type,need to use DjangoJSONEncoder

    from django.core.serializers.json import DjangoJSONEncoder
    return HttpResponse(json.dumps(percentage, cls=DjangoJSONEncoder), content_type="application/json")






