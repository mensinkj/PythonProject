from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from datetime import datetime


templater = get_renderer('homepage')


@view_function
def process_request(request):
	params = {}
	
	# if user is already logged in, send them to the homepage
	if request.user.is_authenticated():
		return HttpResponseRedirect('/homepage/')
	
	form = LoginForm()
	if request.method == 'POST':
		print('>>>>>>>>>>> POST')
		form = LoginForm(request.POST)
		if form.is_valid():
			print('>>>>>>>>>>> VALID')
			#user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			#login(request, user)
			HttpResponseRedirect('/homepage/')
	
	params['form'] = form
	params['auth'] = request.user.is_authenticated()
		
	return templater.render_to_response(request, 'login.html', params) 
		
@view_function
def loginform(request):
	params = {}
	
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			HttpResponseRedirect('/')
	
	params['form'] = form
	
	return templater.render_to_response(request, 'login.loginform.html', params)
	
	
# user edit form
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
	
	# ... add validation for blank stuff
	
	def clean_username(self):
		if len(self.cleaned_data['username']) < 4:
			raise forms.ValidationError('Please enter a username that is at least 4 characters.')
			
		return self.cleaned_data['username']