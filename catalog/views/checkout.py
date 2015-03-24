from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required
import homepage.models as hmod

templater = get_renderer('catalog')

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	params = {
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "product",
	}
	
	form = checkoutForm()
	if request.method == 'POST':
		form = checkoutForm(request.POST)
		if form.is_valid():
				return HttpResponseRedirect('/catalog/thankyou/')
				
				
	params['form'] = form
	
		
	return templater.render_to_response(request, 'checkout.html', params)

class checkoutForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	address = forms.CharField(required=True, min_length=1, max_length=100)
	city = forms.CharField(required=True, min_length=1, max_length=100)
	state = forms.CharField(required=True, min_length=1, max_length=100)
	zip = forms.CharField(required=True, min_length=1, max_length=100)
	credit_card = forms.CharField(required=True, widget=forms.PasswordInput) # label="My Label"
 
@view_function
def gettime(request):
  params = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', params)  