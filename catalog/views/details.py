from django.conf import settings
from django import forms
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod


templater = get_renderer('catalog')

@view_function
def process_request(request):
	params = {
		'now': datetime.now().strftime('%H:%M'),
  		'currentPage': "product",
	}
	
	#get the selected product
	try:
		product = hmod.Product.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		#redirect to users page
		return HttpResponse('Item does not exist. Please go back and try again.')
	
	try:
		photo = hmod.Photograph.objects.get(object_pictured=product)
	except hmod.Photograph.DoesNotExist:
		#fail silently
		pass
	
	form = quantityForm()
	
	params['photo'] = photo
	params['form'] = form
	params['auth'] = request.user.is_authenticated()
	params['product'] = product
	
	## add something to session
	#request.session['hey'] = 'world 1'
	#print('>>>>>>>>>>>>', request.session['hey'])
	
	## add item to the shopping cart (this needs to be done inside the add to cart button)
	#item = hmod.Items.objects.get(id=12341234)
	#if 'shopping_cart' not in request.session:
	#	request.session['shopping_cart'] = {} # use [] for list OR {} for dictionary
	
	# 	# for list
	#	request.session['shopping_cart'].append(item.id)
	
	
	#	# for dictionary
	#	if item.id in request.session['shopping_cart']:
	#		request.session['shopping_cart'][item.id] += 1
	#	else:
	#		request.session['shopping_cart'][item.id] = 1
	
	## How the list would look in the session:
	# [ [1,1], [2, 1], [56, 1] ] <== list
	# { 1: 1, 2: 1, 56: 1 } <== dictionary
	
	# dictionary will be better in this case
		
	return templater.render_to_response(request, 'details.html', params)
  
@view_function
def gettime(request):
  params = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', params)  
  
  
class quantityForm(forms.Form):
	quantity = forms.ChoiceField(choices=[(x, x) for x in range(1, 11)])