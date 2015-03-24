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

import homepage.models as hmod

templater = get_renderer('account')


#########################################
#### Change User Password

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):

	params = {
		# display current time and set current page
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "signup",
	}
	
	params['auth'] = request.user.is_authenticated()
	
	#get current user
	currentid = request.user.id
	userid = request.urlparams[0]
	
	if userid == currentid:
		params['current'] = True
	
	#get the selected user
	try:
		user = hmod.User.objects.get(id=userid)
	except hmod.User.DoesNotExist:
		#redirect to users page
		return HttpResponseRedirect('/')
	
	form = UserEditForm()
	form.userid = user.id
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		#add user id to form
		form.userid = user.id
		if form.is_valid():
			user.set_password(form.cleaned_data['passwordConfirm'])
			user.save()
			
			#re login the user if they are currently logged in.
			if userid == currentid:
				user1 = authenticate(username=request.user.username, password=form.cleaned_data['passwordConfirm'])
				login(request, user1)
				return HttpResponseRedirect('/account/success/')
			else:
				return HttpResponseRedirect('/users.edit/' + userid + '/')
	
	params['userid'] = userid
	params['form'] = form
	
	return templater.render_to_response(request, 'changepass.html', params)
	
class UserEditForm(forms.Form):
	currentPassword = forms.CharField(required=True, label=" Current Password", widget=forms.PasswordInput)
	password = forms.CharField(required=True, label="New Password", widget=forms.PasswordInput)
	passwordConfirm = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput)
	
	def clean_currentPassword(self):
		#get user id
		try:
			user = hmod.User.objects.get(id=self.userid)
		except hmod.SiteUser.DoesNotExist:
			return HttpResponse('Sorry, an error occurred!')
		if (user.check_password(self.cleaned_data['currentPassword']) == False):
			raise forms.ValidationError('Current password is not correct.')
		return self.cleaned_data['currentPassword']		
					
	
	def clean_passwordConfirm(self):
		if self.cleaned_data['password'] != self.cleaned_data['passwordConfirm']:
			raise forms.ValidationError('Passwords do not match!')
		return self.cleaned_data['passwordConfirm']	
  
##############################################################
##### Keeps the time  

@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  