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
  		'currentPage': "areas",
	}
	
	# add the user model
	areas = hmod.Area.objects.all().order_by('name')
	
	# pass variable to html
	params['areas'] = areas
	params['auth'] = request.user.is_authenticated()
	
	print(areas)
	
	#try:
	#	user = hmod.SiteUser.objects.get(id=2)
	#except hmod.SiteUser.DoesNotExist:
		# print('something went wrong')
		# do something here
		# return HttpResponseRedirect('/homepage/')
	
	return templater.render_to_response(request, 'areas.html', params)
  
##############################################################
##### Edits a single area  

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def edit(request):
	params = {}
	
	#debug
	print("Editing Area ID: " + request.urlparams[0])
	
	#get the selected area
	try:
		area = hmod.Area.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		#redirect to areas page
		return HttpResponseRedirect('/homepage/areas/')
	
	#create form
	form = AreaEditForm( initial = {
		'area_name': area.name,
		'description': area.description,
		'place_number': area.place_number,
	})
	if request.method == 'POST':
		form = AreaEditForm(request.POST)
		#add area id to form
		form.areaid = area.photographablething_ptr_id
		if form.is_valid():
			area.name = form.cleaned_data['area_name']
			area.description = form.cleaned_data['description']
			area.place_number = form.cleaned_data['place_number']
			area.save()
			return HttpResponseRedirect('/homepage/areas/')
			
	params['form'] = form
	params['area'] = area
		
	return templater.render_to_response(request, 'areas.edit.html', params) 

#area edit form
class AreaEditForm(forms.Form):
	area_name = forms.CharField(required=True, max_length=100)
	description = forms.CharField(required=True, max_length=200)
	place_number = forms.IntegerField()
	
	def clean_area_name(self):
		#check to see if area_name already exists
		area_count = hmod.Area.objects.filter(name=self.cleaned_data['area_name']).exclude(photographablething_ptr_id=self.areaid).count()
		if area_count >= 1:
			raise forms.ValidationError("This area already exists in the database!")	
	
		if len(self.cleaned_data['area_name']) < 1:
			raise forms.ValidationError('Please enter a name!')
			
		return self.cleaned_data['area_name']
		
		
##############################################################
##### Creates a new area 

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def create(request):
	area1 = hmod.Area()
	area1.name = 'New Area'
	area1.description = 'New Description'
	area1.place_number = 9999
	# ... other field defaults
	area1.save()
	
	return HttpResponseRedirect('/homepage/areas.edit/{}/'.format(area1.photographablething_ptr_id))


##############################################################
##### Deletes a area

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def delete(request):
	try:
		area = hmod.Area.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		return HttpResponseRedirect('/homepage/areas/')
		
	area.delete()
	
	return HttpResponseRedirect('/homepage/areas/')	 
  
  
@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  