from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
import random

import homepage.models as hmod

templater = get_renderer('account')

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	params = {
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "account",
	}
	
	params['auth'] = request.user.is_authenticated()
	params['username'] = request.user.username
	params['first_name'] = request.user.first_name
	params['last_name'] = request.user.last_name
	params['email'] = request.user.email
	params['userid'] = request.user.id
	
	return templater.render_to_response(request, 'index.html', params)
  
@view_function
def gettime(request):
  params = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', params)  
  
