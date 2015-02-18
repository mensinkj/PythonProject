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
	
	# create form
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			
			return HttpResponseRedirect('/homepage/')
			
	params['form'] = form
	params['auth'] = request.user.is_authenticated()
		
	return templater.render_to_response(request, 'login.html', params) 

# user edit form
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
	
	# ... add validation for blank stuff
	
	def clean_username(self):
		if len(self.cleaned_data['username']) < 4:
			raise forms.ValidationError('Please enter a username that is at least 4 characters.')
			
		return self.cleaned_data['username']
	
	## check for actual user
	def clean(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if user == None:
			raise forms.ValidationError('Sorry, the username and/or password you entered is incorrect.')
		print('Authenticated User!')		
		return self.cleaned_data