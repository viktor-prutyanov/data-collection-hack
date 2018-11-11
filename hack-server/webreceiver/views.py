from __future__ import unicode_literals
import ast
import subprocess
import json

from django.shortcuts import render
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from webreceiver.models import Reports

from collections import namedtuple

# Create your views here.
@csrf_exempt
def submit(request):
	print("JSON:", request.body)
	data = json.loads(request.body)
	print("Received JSON:", data)
	push_to_db(data['user_id'], data['lat'], data['lng'], data['time'], data['presence'], data['name'])
	response = HttpResponse('OK', content_type='application/json')
	print(response)
	return response

def load(request):
	rs = Reports.objects.all()
	response = JsonResponse([{'user_id': r.user_id, 'lat': r.lat, 'lng': r.lng, 'time': r.time, 'presence': r.presence, 'name': r.name} for r in rs if r.presence], safe=False)
	print(response)
	return response

def submit2(request):
	return render(request, 'webreceiver/submit2.html', {})

def index(request):
	rs = Reports.objects.all()
	context = {'report_list': rs}
	return render(request, 'webreceiver/index.html', context)

def push_to_db(p1, p2, p3, time, pres, name):
	r = Reports(user_id=int(p1), lat=float(p2), lng=float(p3), time=time, presence=pres, name=name)
	r.save()
