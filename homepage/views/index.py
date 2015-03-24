from django.conf import settings
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random

import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'timecolor': random.choice([ 'red', 'blue', 'green', 'brown' ]),
  		'currentPage': "home",
	}
	
	params['auth'] = request.user.is_authenticated()
	
	return templater.render_to_response(request, 'index.html', params)
  
@view_function
def gettime(request):
  params = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', params)  
  
@view_function
def permission(request):

	params['auth'] = request.user.is_authenticated()
	
	return templater.render_to_response(request, 'index.permission.html', params)
	
@view_function
def check_username(request):
		
	username = request.REQUEST.get('user')
	print('>>>>>>>>>>', username)
	
	# check to see username is taken
	try:
		user = hmod.User.objects.get(username=username)
	except hmod.User.DoesNotExist:
		#bad -- username is taken
		return HttpResponse("0")
	
	#good -- username is not taken
	return HttpResponse("1")
	
	