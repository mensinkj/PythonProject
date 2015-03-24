from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required


templater = get_renderer('account')


##############################################################
##### Shows signup page
@view_function
def process_request(request):

	params = {
		# display current time and set current page
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "signup",
	}
	
	#create form
	form = NewUserForm()
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			#create the user
			user1 = hmod.User()
			user1.username = form.cleaned_data['username']
			user1.email = form.cleaned_data['email']
			user1.first_name = form.cleaned_data['first_name']
			user1.last_name = form.cleaned_data['last_name']
			user1.set_password(form.cleaned_data['passwordConfirm'])
			
			## TODO: add user to group 
			
			
			# ... other field defaults
			user1.save()
			
			# login the newly created user
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['passwordConfirm'])
			login(request, user)
			return HttpResponseRedirect('/index/')
			#return HttpResponse('It worked!!')
	
	params['form'] = form
	params['auth'] = request.user.is_authenticated()
	
	
	return templater.render_to_response(request, 'signup.html', params)
  
  
class NewUserForm(forms.Form):
	username = forms.CharField(required=True, min_length=1, max_length=100)
	first_name = forms.CharField(required=True, min_length=1, max_length=100)
	last_name = forms.CharField(required=True, min_length=1, max_length=100)
	email = forms.EmailField(required=True, min_length=1, max_length=100)
	password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput)
	passwordConfirm = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput)
	
	def clean_passwordConfirm(self):
		if self.cleaned_data['password'] != self.cleaned_data['passwordConfirm']:
			raise forms.ValidationError('Passwords do not match!')
		return self.cleaned_data['passwordConfirm']
		
	def clean_username(self):
		#check to see if username already exists
		user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).count()
		if user_count >= 1:
			raise forms.ValidationError("This username is already taken.")	
	
		if len(self.cleaned_data['username']) < 4:
			raise forms.ValidationError('Please enter a username that is at least 4 characters.')
			
		return self.cleaned_data['username']


##############################################################
##### Shows signup page
@view_function
def create_user(request):

	params = { }
	
	#create form
	form = NewUserForm()
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			#create the user
			user1 = hmod.User()
			user1.username = form.cleaned_data['username']
			user1.email = form.cleaned_data['email']
			user1.first_name = form.cleaned_data['first_name']
			user1.last_name = form.cleaned_data['last_name']
			user1.set_password(form.cleaned_data['passwordConfirm'])
			
			## TODO: add user to group 
			
			
			# ... other field defaults
			user1.save()
			
			# login the newly created user
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['passwordConfirm'])
			login(request, user)
			return HttpResponseRedirect('/')
			#return HttpResponse('It worked!!')
	
	params['form'] = form
	params['auth'] = request.user.is_authenticated()
	
	
	return templater.render_to_response(request, 'signup.create_user.html', params)


##############################################################
##### Keeps the time  

@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  