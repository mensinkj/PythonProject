from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest

import homepage.models as hmod


templater = get_renderer('catalog')

@view_function
def process_request(request):
	params = {
		'now': datetime.now().strftime(request.urlparams[0] if request.urlparams[0] else '%H:%M'),
  		'currentPage': "product",
	}
	
	params['auth'] = request.user.is_authenticated()
	
	# add the product model
	products = hmod.Product.objects.all().order_by("name")
	photos = hmod.Photograph.objects.all()
	
	params['photos'] = photos
	params['products'] = products
	
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
		
	return templater.render_to_response(request, 'index.html', params)

@view_function
def search(request):
	params = {}

	products = hmod.Product.objects.filter(name__icontains=request.urlparams[0])
	photos_db = hmod.Photograph.objects.all()
	
	productCount = hmod.Product.objects.filter(name__icontains=request.urlparams[0]).count()
	
	params['products'] = products
	params['productCount'] = productCount
	
	return templater.render_to_response(request, 'index.search.html', params)

 
@view_function
def gettime(request):
  params = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', params)  