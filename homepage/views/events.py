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
  		'currentPage': "events",
	}
	
	# add the user model
	events = hmod.Event.objects.all().order_by('start_date')
	
	# pass variable to html
	params['events'] = events
	params['auth'] = request.user.is_authenticated()
	
	print(events)
	
	#try:
	#	user = hmod.SiteUser.objects.get(id=2)
	#except hmod.SiteUser.DoesNotExist:
		# print('something went wrong')
		# do something here
		# return HttpResponseRedirect('/homepage/')
	
	return templater.render_to_response(request, 'events.html', params)
  	
  
##############################################################
##### Edits a single event  

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def edit(request):
	params = {}
	
	#debug
	print("Editing Event ID: " + request.urlparams[0])
	
	#get the selected event
	try:
		event = hmod.Event.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Event.DoesNotExist:
		#redirect to events page
		return HttpResponseRedirect('/homepage/events/')
	
	#create form
	form = EventEditForm( initial = {
		'event_name': event.name,
		'start_date': event.start_date,
		'end_date': event.end_date,
		'map_file': event.map_file,
	})
	if request.method == 'POST':
		form = EventEditForm(request.POST)
		#add event id to form
		form.eventid = event.photographablething_ptr_id
		if form.is_valid():
			event.name = form.cleaned_data['event_name']
			event.start_date = form.cleaned_data['start_date']
			event.end_date = form.cleaned_data['end_date']
			event.map_file = form.cleaned_data['map_file']
			event.save()
			return HttpResponseRedirect('/homepage/events/')
			
	params['form'] = form
	params['event'] = event
		
	return templater.render_to_response(request, 'events.edit.html', params) 

#event edit form
class EventEditForm(forms.Form):
	event_name = forms.CharField(required=True, max_length=100)
	start_date = forms.DateTimeField()
	end_date = forms.DateTimeField()
	map_file = forms.CharField(required=False, max_length=100)
	
	def clean_event_name(self):
		#check to see if event_name already exists
		event_count = hmod.Event.objects.filter(name=self.cleaned_data['event_name']).exclude(photographablething_ptr_id=self.eventid).count()
		if event_count >= 1:
			# ... eventually add checking for dates
			raise forms.ValidationError("This event already exists in the database!")	
	
		if len(self.cleaned_data['event_name']) < 1:
			raise forms.ValidationError('Please enter a name!')
			
		return self.cleaned_data['event_name']
		
		
##############################################################
##### Creates a new event 

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def create(request):
	event1 = hmod.Event()
	event1.name = 'New Event'
	event1.start_date = '2015-1-1'
	event1.end_date = "2015-1-31"
	map_file = ''
	# ... other field defaults
	event1.save()
	
	return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event1.photographablething_ptr_id))


##############################################################
##### Deletes a event

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def delete(request):
	try:
		event = hmod.Event.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Event.DoesNotExist:
		return HttpResponseRedirect('/homepage/events/')
		
	event.delete()
	
	return HttpResponseRedirect('/homepage/events/')	    
  
@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  