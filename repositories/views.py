from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import requests
import json
from django.http import HttpResponseRedirect
from django.template  import RequestContext
import os
from bluebird.settings import API_ENDPOINT
import logging
from requests.exceptions import ConnectionError


LOG=logging.getLogger('django')


# Create your views here.


def index(request):
    project_id = request.GET.get('project_id')
    url = '%s/repos?project_id=%s' % (API_ENDPOINT,project_id)  
    headers={'Content-Type':'application/json'}
    try:
        resp = requests.get(url,headers=headers)
        repos = resp.json()
    except ConnectionError:
        repos = []
    return render_to_response('repos-replace.html',{'repos': repos})

def show(request):
    return HttpResponseRedirect('/repositories/')

def create(request):
    if request.method == 'POST':
        project_id=request.POST.get('project_id').strip()
        path=request.POST.get('path').strip()
        data = {
                'project_id' : project_id, 
                'path' : path,
        }
        url='{}/repos'.format(API_ENDPOINT)
        headers={'Content-Type':'application/json'}
        try:
            requests.post(url,headers=headers,data=json.dumps(data))
        except ConnectionError:
            LOG.info("add repo {} failed".format(path))
     
    return HttpResponse("ok")

def update(request):
    return HttpResponseRedirect('/repositories/')


def delete(request):
    return HttpResponseRedirect('/repositories/')

def list(request):
    project_id = request.GET.get('project_id')
    url = '%s/repos?project_id=%s' % (API_ENDPOINT,project_id)  
    headers={'Content-Type':'application/json'}
    try:
        resp = requests.get(url,headers=headers)
        repos = resp.json()
    except ConnectionError:
        repos = []
    return HttpResponse(json.dumps(repos))

