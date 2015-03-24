from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from datetime import datetime


templater = get_renderer('account')


@view_function
def process_request(request):
	params = {}
	
	# if user is already logged in, send them to the homepage
	if request.user.is_authenticated():
		return HttpResponseRedirect('/homepage/')
	
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			
			login(request, user)
			return HttpResponseRedirect('/catalog/')
			
			
	params['form'] = form
		
	return templater.render_to_response(request, 'login.html', params) 
	
	
@view_function
def loginform(request):
	params = {}
	
	# if user is already logged in, send them to the homepage
	if request.user.is_authenticated():
		return HttpResponseRedirect('/homepage/')
	
	print('>>>>>>>>>>>>>>>>> Page Loaded')
	form = LoginForm()
	print('>>>>>>>>>>>>>>>>> Form Created')
	if request.method == 'POST':
		print('>>>>>>>>>>>>>>>>> POST')
		form = LoginForm(request.POST)
		if form.is_valid():
			print('>>>>>>>>>>>>>>>>> VALID!')
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			print('>>>>>>>>>>>>>>>>> Supposed to login...')
			
			
	params['form'] = form
		
	return templater.render_to_response(request, 'login.loginform.html', params) 	

	
# user edit form
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
	
	# ... add validation for blank stuff
	
	#def clean_username(self):
	#	if len(self.cleaned_data['username']) < 1:
	#		raise forms.ValidationError('Please enter a username.')
			
	#	return self.cleaned_data['username']
		
	#def clean_password(self):
	#	if len(self.cleaned_data['password']) < 1 :
	#		raise forms.ValidationError('Please enter a password.')			
	#	return self.cleaned_data['password']
		
		#### TODO: Fix - for some reason this doesn't work with blank passwords....
	#	def clean(self):
	#		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
	#		if user == None:
	#			raise forms.ValidationError("Invalid Credentials.")
	#		return self.cleaned_data	