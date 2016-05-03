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

def index(request):
    """show all projects."""
    url='{}/projects'.format(API_ENDPOINT)
    headers={'Content-Type':'application/json'}
    try:
        resp = requests.get("{}/projects".format(API_ENDPOINT),headers=headers)
        projects=resp.json()
    except ConnectionError:
	projects = []
    return render_to_response('projects.html',
                              {'projects':projects},
                             context_instance=RequestContext(request))

def show(request):
    project_id=os.path.basename(request.path)
    url='{}/projects/{}'.format(API_ENDPOINT,project_id)
    headers={'Content-Type':'application/json'}
    try:
        resp = requests.get(url,headers=headers)
        project = resp.json()
    	print(project['id'])
    except ConnectionError:
        project = {}
    return render_to_response("project.html",
                              {"project": project},
                               context_instance=RequestContext(request))


def update(request):
    project_id=os.path.basename(request.path)
    project_name = request.GET['name']
    project_desc =  request.GET['desc']
    project_members = request.GET['members']
    project_hgs = request.GET['hgs']
    url='{}/projects/{}?name={}&desc={}&members={}&hgs={}'.format(API_ENDPOINT,project_id,project_name,project_desc,project_members,project_hgs)
    headers={'Content-Type':'application/json'}
    rs = requests.put(url,headers=headers)
    return  HttpResponse(json.dumps(rs.json()))

def create(request):
    if request.method == 'POST':
        name=request.POST.get('name').strip()
        desc=request.POST.get('desc').strip()
        data = {
                'name' : name, 
                'desc' : desc,
        }
        url='{}/projects'.format(API_ENDPOINT)
        headers={'Content-Type':'application/json'}
        try:
            requests.post(url,headers=headers,data=json.dumps(data))
        except ConnectionError:
            LOG.info("create prject {} failed".format(name))
     
    return HttpResponseRedirect('/projects/')

def delete(request):
    project_id=request.GET['id']
    url = '{}/projects/{}'.format(API_ENDPOINT,project_id)
    headers={'Content-Type':'application/json'}
    rs = requests.delete(url,headers=headers)
    #return HttpResponseRedirect('/admin/files')
    return HttpResponse("succeed")

    
def admin(request):
    return render_to_response('projects/admin.html')

