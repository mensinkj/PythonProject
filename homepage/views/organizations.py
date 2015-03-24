from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
import homepage.models as hmod
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required


templater = get_renderer('homepage')

@view_function
@login_required(login_url='/homepage/login/')
def process_request(request):

	params = {
		# display current time and set current page
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "organizations",
	}
	
	# add the user model
	organizations = hmod.Organization.objects.all().order_by('given_name')
	
	# pass variable to html
	params['organizations'] = organizations
	params['auth'] = request.user.is_authenticated()
	
	print(organizations)
	
	#try:
	#	user = hmod.SiteUser.objects.get(id=2)
	#except hmod.SiteUser.DoesNotExist:
		# print('something went wrong')
		# do something here
		# return HttpResponseRedirect('/homepage/')
	
	return templater.render_to_response(request, 'organizations.html', params)
  
##############################################################
##### Edits a single organization  

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def edit(request):
	params = {}
	
	#debug
	print("Editing Organization ID: " + request.urlparams[0])
	
	#get the selected organization
	try:
		organization = hmod.Organization.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Organization.DoesNotExist:
		#redirect to organizations page
		return HttpResponseRedirect('/homepage/organizations/')
	
	#create form
	form = OrganizationEditForm( initial = {
		'organization_name': organization.given_name,
		'type': organization.organization_type,
		'creation_date': organization.creation_date,
	})
	if request.method == 'POST':
		form = OrganizationEditForm(request.POST)
		#add organization id to form
		form.organizationid = organization.photographablething_ptr_id
		if form.is_valid():
			organization.given_name = form.cleaned_data['organization_name']
			organization.organization_type = form.cleaned_data['type']
			organization.creation_date = form.cleaned_data['creation_date']
			organization.save()
			return HttpResponseRedirect('/homepage/organizations/')
			
	params['form'] = form
	params['organization'] = organization
		
	return templater.render_to_response(request, 'organizations.edit.html', params) 

#organization edit form
class OrganizationEditForm(forms.Form):
	organization_name = forms.CharField(required=True, min_length=1, max_length=100)
	type = forms.CharField(required=False, min_length=1, max_length=100)
	creation_date = forms.DateTimeField(required=True)
	
	def clean_organization_name(self):
		#check to see if organization_name already exists
		organization_count = hmod.Organization.objects.filter(given_name=self.cleaned_data['organization_name']).exclude(photographablething_ptr_id=self.organizationid).count()
		if organization_count >= 1:
			raise forms.ValidationError("This organization already exists in the database!")	
	
		if len(self.cleaned_data['organization_name']) < 1:
			raise forms.ValidationError('Please enter a name!')
			
		return self.cleaned_data['organization_name']
		
		
##############################################################
##### Creates a new organization 

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def create(request):
	organization1 = hmod.Organization()
	organization1.given_name = 'New Organization'
	organization1.organization_type = ''
	organization1.creation_date = "2001-12-31"
	# ... other field defaults
	organization1.save()
	
	return HttpResponseRedirect('/homepage/organizations.edit/{}/'.format(organization1.photographablething_ptr_id))


##############################################################
##### Deletes a organization

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def delete(request):
	try:
		organization = hmod.Organization.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Organization.DoesNotExist:
		return HttpResponseRedirect('/homepage/organizations/')
		
	organization.delete()
	
	return HttpResponseRedirect('/homepage/organizations/')	  
    
  
  
@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  