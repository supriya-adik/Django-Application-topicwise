from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request) :
    emp = {'id':101,'name':"Supriya",'address':"pune"}
    data = json.dumps(emp)
    return HttpResponse(data,content_type="application/json")