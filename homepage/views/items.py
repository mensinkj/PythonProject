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
  		'currentPage': "items",
	}
	
	# add the user model
	items = hmod.Item.objects.all().order_by('name')
	
	# pass variable to html
	params['items'] = items
	params['auth'] = request.user.is_authenticated()
	
	print(items)
	
	#try:
	#	user = hmod.SiteUser.objects.get(id=2)
	#except hmod.SiteUser.DoesNotExist:
		# print('something went wrong')
		# do something here
		# return HttpResponseRedirect('/homepage/')
	
	return templater.render_to_response(request, 'items.html', params)
  
  
##############################################################
##### Edits a single item  

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def edit(request):
	params = {}
	
	#debug
	print("Editing Item ID: " + request.urlparams[0])
	
	#get the selected item
	try:
		item = hmod.Item.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		#redirect to items page
		return HttpResponseRedirect('/homepage/items/')
	
	#create form
	form = ItemEditForm( initial = {
		'item_name': item.name,
		'description': item.description,
		'value': item.value,
		'standard_rental_price': item.standard_rental_price,
	})
	if request.method == 'POST':
		form = ItemEditForm(request.POST)
		#add item id to form
		form.itemid = item.photographablething_ptr_id
		if form.is_valid():
			item.name = form.cleaned_data['item_name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.standard_rental_price = form.cleaned_data['standard_rental_price']
			item.save()
			return HttpResponseRedirect('/homepage/items/')
			
	params['form'] = form
	params['item'] = item
		
	return templater.render_to_response(request, 'items.edit.html', params) 

#item edit form
class ItemEditForm(forms.Form):
	item_name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=False, min_length=1, max_length=1000)
	value = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
	standard_rental_price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
	
	def clean_item_name(self):
		#check to see if itemname already exists
		item_count = hmod.Item.objects.filter(name=self.cleaned_data['item_name']).exclude(photographablething_ptr_id=self.itemid).count()
		if item_count >= 1:
			raise forms.ValidationError("This item already exists!")	
	
		if len(self.cleaned_data['item_name']) < 1:
			raise forms.ValidationError('Please enter a name!')
			
		return self.cleaned_data['item_name']
		
		
##############################################################
##### Creates a new item 

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def create(request):
	item1 = hmod.Item()
	item1.name = 'NewItem'
	item1.description = ''
	item1.value = 0.00
	item1.standard_rental_price = 0.00
	# ... other field defaults
	item1.save()
	
	return HttpResponseRedirect('/homepage/items.edit/{}/'.format(item1.photographablething_ptr_id))


##############################################################
##### Deletes a item

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def delete(request):
	try:
		item = hmod.Item.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')
		
	item.delete()
	
	return HttpResponseRedirect('/homepage/items/')	  
    
  
  
@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  