# Updated 1-27-2015 by Jameson. Changed the model slightly to allow it to build with PostgreSQL rather than SQLite.
from django.db import models
from polymorphic import PolymorphicModel
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	address1 = models.TextField(max_length=100)
	
	
class PhotographableThing(PolymorphicModel):
	object_id = models.AutoField(primary_key=True)

class LegalEntity(PhotographableThing):
	given_name = models.TextField(max_length=50)
	creation_date = models.DateTimeField()
	address1 = models.TextField(max_length=100, null=True)
	address2 = models.TextField(max_length=100, null=True)
	city = models.TextField(max_length=30, null=True)
	state = models.TextField(max_length=30, null=True)
	zip_code = models.IntegerField(max_length=5, null=True)
	email = models.EmailField(max_length=75, null=True)

class Person(LegalEntity):
	family_name = models.TextField(max_length=30)
	
class Organization(LegalEntity):
	organization_type = models.TextField(max_length=30, null=True)

class Agent(Person):
	appointment_date = models.DateField()

class Participant(Person):
	biographical_sketch = models.TextField(max_length=1000, null=True)
	contact_relationship = models.TextField(max_length=30, null=True)
	id_photo = models.FilePathField(null=True)
	emergency_contact = models.ForeignKey('Person', related_name='+')

class Role(models.Model):
	area_id = models.ForeignKey('Area')
	participant_id = models.ForeignKey('Participant')
	name = models.TextField(max_length=50)
	role_type = models.TextField(max_length=50)

	class Meta:
		unique_together = ('area_id' , 'participant_id')

class Item(PhotographableThing):
	legal_entity_id = models.ForeignKey('LegalEntity', null=True)
	name = models.TextField(max_length=50)
	description = models.TextField(max_length=200)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	standard_rental_price = models.DecimalField(max_digits=10, decimal_places=2)

class WardrobeItem(Item):
	size = models.TextField(max_length=15)
	size_modifier = models.TextField(max_length=30)
	gender = models.TextField(max_length=6)
	color = models.TextField(max_length=20)
	pattern = models.TextField(max_length=30)
	start_year = models.IntegerField(max_length=4)
	end_year = models.IntegerField(max_length=4)
	note = models.TextField(max_length=200)
	
class RentableItem(Item):
	rentable_item_id = models.ForeignKey('Item', related_name='+')
	#empty class to store rentable items primary keys


class Phone(models.Model):
	phone_id = models.AutoField(primary_key=True)
	legal_entity_id = models.ForeignKey('LegalEntity')
	number = models.TextField(max_length=15)
	extension = models.TextField(max_length=9)
	phone_type = models.TextField(max_length=8)

class Rental(models.Model):
	rental_id = models.AutoField(primary_key=True)
	customer = models.ForeignKey('Organization', null=True, related_name='+')
	contact = models.ForeignKey('Person' , null=True, related_name='+') ## null should be set to False, but for dev this works
	issuer = models.ForeignKey('Agent' , null=True, related_name='+') ## null should be set to False, but for dev this works
	rental_time = models.DateTimeField()
	due_date = models.DateTimeField()
	discount_percent = models.IntegerField(null=True, max_length=2)

class Product(PhotographableThing):
	owner = models.ForeignKey('LegalEntity', null=True)
	name = models.TextField(max_length=20)
	description = models.TextField(max_length=200)
	category = models.TextField(max_length=30)
	current_price = models.DecimalField(max_digits=10, decimal_places=2)

class ProductPicture(PhotographableThing):
	product = models.ForeignKey('Product' , null=False)
	picture = models.FilePathField()
	caption = models.TextField(max_length=100)

class BulkProduct(Product):
	quantity_on_hand = models.IntegerField(max_length=6)

class IndividualProduct(Product):
	date_made = models.DateField()

class PersonalProduct(Product):
	order_form_name = models.TextField(max_length=30)
	production_minutes = models.IntegerField()

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	shipper = models.ForeignKey('Agent' , null=True, related_name='+')
	packer = models.ForeignKey('Agent' , null=True, related_name='+')
	payment_processor = models.ForeignKey('Agent' , null=True, related_name='+')
	product = models.ForeignKey('IndividualProduct' , null=False)
	order_date = models.DateTimeField()
	phone = models.IntegerField(max_length=12)
	date_packed = models.DateTimeField()
	date_shipped = models.DateTimeField()
	date_paid = models.DateTimeField()
	tracking_number = models.TextField(max_length=50)

class BulkDetail(models.Model):
	order_id = models.ForeignKey('Order')
	bulk_product_id = models.ForeignKey('BulkProduct')
	quantity = models.IntegerField(max_length=6)
	price = models.DecimalField(max_digits=10 , decimal_places=2)

	class Meta:
		unique_together = ('order_id' , 'bulk_product_id')

class PersonalDetail(models.Model):
	order_id = models.ForeignKey('Order')
	personal_product_id = models.ForeignKey('PersonalProduct')
	order_file = models.FilePathField()

	class Meta:
		unique_together = ('order_id' , 'personal_product_id')

class Area(PhotographableThing):
	name = models.TextField(max_length=50)
	event_id = models.ForeignKey('Event' , null=True)
	description = models.TextField(max_length=200)
	place_number = models.IntegerField()

class Event(PhotographableThing):
	name = models.TextField(max_length=100, null=False)
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)
	map_file = models.FilePathField(null=True)

class Venue(PhotographableThing):
	event_id = models.ForeignKey('Event' , null=True)
	name = models.TextField(max_length=50)
	address = models.TextField(max_length=150)
	city = models.TextField(max_length=50)
	state = models.TextField(max_length=20)
	zip_code = models.IntegerField(max_length=5) 

class PublicEvent(PhotographableThing):
	name = models.TextField(max_length=50)
	description = models.TextField(max_length=200)
	event_id = models.ForeignKey('Event' , null=False)

class SaleItem(PhotographableThing):
	area_id = models.ForeignKey('Area' , null=True)
	name = models.TextField(max_length=30)
	description = models.TextField(max_length=200)
	low_price = models.DecimalField(max_digits=10, decimal_places=2)
	high_price = models.DecimalField(max_digits=10, decimal_places=2)

class ItemReturn(models.Model):
	item_return_id = models.AutoField(primary_key=True)
	return_agent_id = models.ForeignKey('Agent',null=True)
	return_time = models.DateTimeField()
	fees_paid = models.BooleanField(default=False)

class RentedItem(models.Model):
	rentable_item_id = models.ForeignKey('RentableItem', null=False)
	rental_id = models.ForeignKey('Rental', null=False)
	item_return_id = models.ForeignKey('ItemReturn', null=True)
	condition = models.TextField(max_length=200)
	new_damage = models.TextField(max_length=200)
	damage_fee = models.DecimalField(max_digits=10, decimal_places=2)
	late_fee = models.DecimalField(max_digits=6, decimal_places=2)

	class Meta:
		unique_together = ('rentable_item_id' , 'rental_id')

class Photograph(models.Model):
	photograph_id = models.AutoField(primary_key=True)
	photographer_id = models.ForeignKey('Person' , null=True)
	object_pictured = models.ForeignKey('PhotographableThing', null = False, related_name="+")
	date_taken = models.DateTimeField(null=True)
	place_taken = models.TextField(max_length=50, null=True)
	image = models.TextField(null=True)

