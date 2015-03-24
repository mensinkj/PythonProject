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
	shopping_cart = request.session['shopping_cart']
	# get each product in the shopping cart
	cart = hmod.Product.objects.filter(photographablething_ptr_id__in=request.session['shopping_cart'])
	
	params['session_cart'] = request.session['shopping_cart']
	
	print('>>>>>>>>>>>>>>>>>> Session Output:', request.session['shopping_cart'])
	#print('>>>>>>>>>>>>>>>>>>>>>', shopping_cart['3'])
	
	params['cart'] = cart
	
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
		
	return templater.render_to_response(request, 'cart.html', params)


@view_function
def add(request):
	params = {}
	
	print('>>>>>>>>>>>>>>>>>> Item ID: ' + request.urlparams[0])
	print('>>>>>>>>>>>>>>>>>> Quantity: ' + request.urlparams[1])
	
	## add shopping cart to session
	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {} 

	# If item.id is already in shopping_cart, increment it by qty added, otherwise, set item.id as qty added
	if request.urlparams[0] in request.session['shopping_cart']:
		request.session['shopping_cart'][request.urlparams[0]] = int(request.session['shopping_cart'][request.urlparams[0]]) + int(request.urlparams[1])
	else:
		request.session['shopping_cart'][request.urlparams[0]] = int(request.urlparams[1])

	print('>>>>>>>>>>>>>>>>>> Session Output:', request.session['shopping_cart'])
	
	# Save session variable changes
	request.session.modified = True
	
	# delete for debug
	#del request.session['shopping_cart']
	
	return HttpResponseRedirect("/catalog/cart/")
	
	
@view_function
def delete(request):
	
	print('>>>>>>>>>>>>>>>>>> Item ID: ' + request.urlparams[0])
	
	## add shopping cart to session
	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {} 

	del request.session['shopping_cart'][request.urlparams[0]]

	print('>>>>>>>>>>>>>>>>>> Session Output:', request.session['shopping_cart'])
	
	# Save session variable changes
	request.session.modified = True
	
	return HttpResponseRedirect('/catalog/cart/')
	