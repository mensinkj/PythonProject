from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from datetime import datetime
from django.contrib.auth.decorators import login_required


templater = get_renderer('homepage')


@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):
	params = {}
	#logout user
	logout(request)
    
    # Redirect to a success page.
		
	return templater.render_to_response(request, 'logout.html', params) 