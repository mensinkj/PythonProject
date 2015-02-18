from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required


templater = get_renderer('homepage')


##############################################################
##### Shows the list of users
@view_function
#require login
@login_required(login_url='/homepage/login/')
def process_request(request):

	params = {
		# display current time and set current page
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "users",
	}
	
	# add the user model
	users = hmod.User.objects.all().order_by('first_name')
	
	# pass variable to html and sort
	params['users'] = users
	params['auth'] = request.user.is_authenticated()
	
	print(users)
	
	#try:
	#	user = hmod.SiteUser.objects.get(id=2)
	#except hmod.SiteUser.DoesNotExist:
		# print('something went wrong')
		# do something here
		# return HttpResponseRedirect('/homepage/')
	
	return templater.render_to_response(request, 'users.html', params)
  
  
  
##############################################################
##### Edits a single user  

@view_function
@permission_required('homepage.change_user')
@login_required(login_url='/homepage/login/')
def edit(request):
	params = {}
	
	#debug
	print("Editing User ID: " + request.urlparams[0])
	
	#get the selected user
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		#redirect to users page
		return HttpResponseRedirect('/homepage/users/')
	
	#create form
	form = UserEditForm( initial = {
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
	})
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		#add user id to form
		form.userid = user.id
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			#change the password if it's not empty
			if len(form.cleaned_data['password']) > 0:
				print('Changing the user''s password!')
				user.set_password(form.cleaned_data['password'])
			user.save()
			return HttpResponseRedirect('/homepage/users/')
			
	params['form'] = form
	params['user'] = user
		
	return templater.render_to_response(request, 'users.edit.html', params) 

#user edit form
class UserEditForm(forms.Form):
	username = forms.CharField(required=True, min_length=1, max_length=100)
	first_name = forms.CharField(required=True, min_length=1, max_length=100)
	last_name = forms.CharField(required=True, min_length=1, max_length=100)
	email = forms.EmailField(required=True, min_length=1, max_length=100)
	password = forms.CharField(required=False, label="Password", widget=forms.PasswordInput)
	
	def clean_username(self):
		#check to see if username already exists
		user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if user_count >= 1:
			raise forms.ValidationError("This username is already taken.")	
	
		if len(self.cleaned_data['username']) < 4:
			raise forms.ValidationError('Please enter a username that is at least 4 characters.')
			
		return self.cleaned_data['username']
	
		
##############################################################
##### Creates a new user 

@view_function
@permission_required('homepage.add_user')
@login_required(login_url='/homepage/login/')
def create(request):
	user1 = hmod.User()
	user1.username = 'NewUser'
	user1.email = ''
	user1.first_name = ''
	user1.last_name = ''
	# ... other field defaults
	user1.save()
	
	return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user1.id))


##############################################################
##### Deletes a user 

@view_function
@permission_required('homepage.delete_user')
@login_required(login_url='/homepage/login/')
def delete(request):
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')
		
	user.delete()
	
	return HttpResponseRedirect('/homepage/users/')	


##############################################################
##### Keeps the time  

@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  