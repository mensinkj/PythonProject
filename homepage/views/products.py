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
  		'currentPage': "products",
	}
	
	# add the product model
	products = hmod.Product.objects.all().order_by('name')
	
	# pass variable to html
	params['products'] = products
	params['auth'] = request.user.is_authenticated()
	
	print(products)
	
	#try:
	#	product = hmod.Siteproduct.objects.get(id=2)
	#except hmod.Siteproduct.DoesNotExist:
		# print('something went wrong')
		# do something here
		# return HttpResponseRedirect('/homepage/')
	
	return templater.render_to_response(request, 'products.html', params)
  
##############################################################
##### Edits a single product  

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def edit(request):
	params = {}
	
	#debug
	print("Editing Product ID: " + request.urlparams[0])
	
	#get the selected product
	try:
		product = hmod.Product.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		#redirect to products page
		return HttpResponseRedirect('/homepage/products/')
	
	#create form
	form = ProductEditForm( initial = {
		'product_name': product.name,
		'description': product.description,
		'category': product.category,
		'current_price': product.current_price,
	})
	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		#add product id to form
		form.productid = product.photographablething_ptr_id
		if form.is_valid():
			product.name = form.cleaned_data['product_name']
			product.description = form.cleaned_data['description']
			product.category = form.cleaned_data['category']
			product.current_price = form.cleaned_data['current_price']
			product.save()
			return HttpResponseRedirect('/homepage/products/')
			
	params['form'] = form
	params['product'] = product
		
	return templater.render_to_response(request, 'products.edit.html', params) 

#product edit form
class ProductEditForm(forms.Form):
	product_name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=False, min_length=1, max_length=1000)
	category = forms.CharField(required=False, min_length=1, max_length=100)
	current_price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
	
	def clean_product_name(self):
		#check to see if productname already exists
		product_count = hmod.Product.objects.filter(name=self.cleaned_data['product_name']).exclude(photographablething_ptr_id=self.productid).count()
		if product_count >= 1:
			raise forms.ValidationError("This item already exists!")	
	
		if len(self.cleaned_data['product_name']) < 1:
			raise forms.ValidationError('Please enter a name!')
			
		return self.cleaned_data['product_name']
		
		
##############################################################
##### Creates a new product 

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def create(request):
	product1 = hmod.Product()
	product1.name = 'NewProduct'
	product1.description = ''
	product1.category = ''
	product1.current_price = 0.00
	# ... other field defaults
	product1.save()
	
	return HttpResponseRedirect('/homepage/products.edit/{}/'.format(product1.photographablething_ptr_id))


##############################################################
##### Deletes a product

@view_function
@permission_required('homepage.manager_rights')
@login_required(login_url='/homepage/login/')
def delete(request):
	try:
		product = hmod.Product.objects.get(photographablething_ptr_id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')
		
	product.delete()
	
	return HttpResponseRedirect('/homepage/products/')	  
  
  
@view_function
def gettime(request):
  template_vars = {
	'now': datetime.now(),
  }
  return templater.render_to_response(request, 'index_time.html', template_vars)  