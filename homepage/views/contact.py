from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params = {
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'timecolor': random.choice([ 'red', 'blue', 'green', 'brown' ]),
  		'currentPage': "contact",
	}
	
	params['auth'] = request.user.is_authenticated()
	
	return templater.render_to_response(request, 'contact.html', params)
  
@view_function
def gettime(request):
  params = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', params)  