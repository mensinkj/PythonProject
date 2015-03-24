#!/usr/bin/env python3

import random
import os
import datetime
import sys

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'INTEX.settings'
import homepage.models as hmod
import django
django.setup()

from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

## Drop Database and recreate it

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

## Create group permissions
Permission.objects.all().delete()
Group.objects.all().delete()

permission = Permission()
permission.codename = 'manager_rights'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Has Manager Rights'
permission.save()

permission1 = Permission()
permission1.codename = 'admin_rights'
permission1.content_type = ContentType.objects.get(id=7)
permission1.name = 'Has Admin Rights'
permission1.save()

group1 = Group()
group1.name = "Admin"
group1.save()
group1.permissions.add(permission)
group1.permissions.add(permission1)

group2 = Group()
group2.name = "Managers"
group2.save()
group2.permissions.add(permission1)

group3 = Group()
group3.name = "Guest"
group3.save()


print('permissions initialized')

############ MAKE USERS ####################

hmod.User.objects.all().delete()


user1 = hmod.User()
user1.first_name = "Jameson"
user1.last_name = "Ricks"
user1.username = "jricks92"
user1.email = "jameson@glenricks.com"
user1.is_superuser = 'TRUE'
user1.is_staff = 'TRUE'
user1.set_password('jameson526')
user1.save()
group1.user_set.add(user1)

user3 = hmod.User()
user3.first_name = "Captain"
user3.last_name = "Kirk"
user3.username = "captkirk"
user3.email = "ck@ussenterprise.com"
user3.set_password('kirk789')
user3.save()

user4 = hmod.User()
user4.first_name = "Anakin"
user4.last_name = "Skywalker"
user4.username = "vader"
user4.email = "vader4ever@sithlords.biz"
user4.set_password('padme')
user4.save()

## Products and Photographs:
p1=hmod.Product()
p1.name = "Minted Coin"
p1.description = "Metal coin replica of olonial money. Has Colonial Heritage Foundation logo on it."
p1.category = "Mass Produced"
p1.current_price = 3.99
p1.save()

photo = hmod.Photograph()
photo.object_pictured = p1
photo.image = "https://www.regalassets.com/images/indian-head-coins-F.jpg"
photo.save()


p1=hmod.Product()
p1.name = "Photo of George Washington"
p1.description = "One of our founding fathers."
p1.category = "Mass Produced"
p1.current_price = 3.99
p1.save()

photo = hmod.Photograph()
photo.object_pictured = p1
photo.image = "http://www.nndb.com/people/107/000024035/1pres.jpg"
photo.save()

p1=hmod.Product()
p1.name = "Handcrafted basket"
p1.description = "Basket with your name on it."
p1.category = "Made to Order"
p1.current_price = 9.99
p1.save()

photo = hmod.Photograph()
photo.object_pictured = p1
photo.image = "https://www.connectedgoods.com/images/fair-trade-product_lg/nesting-taupe.jpg"
photo.save()

p1=hmod.Product()
p1.name = "Wooden Toy Gun"
p1.description = "Toy gun that shoots rubber bands."
p1.category = "Mass Produced"
p1.current_price = 6.99
p1.save()

photo = hmod.Photograph()
photo.object_pictured = p1
photo.image = "http://www.urbangifts.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/w/o/wooden-rubberband-gun.jpg"
photo.save()

p1=hmod.Product()
p1.name = "Declaration of Independence"
p1.description = "Replica of the Declaration of Independence"
p1.category = "Mass Produced"
p1.current_price = 3.99
p1.save()

photo = hmod.Photograph()
photo.object_pictured = p1
photo.image = "http://www.loc.gov/rr/program/bib/ourdocs/Images/declaration.jpg"
photo.save()


## Items:
i1=hmod.Item()
i1.name = "Musket"
i1.description = "A colonial era musket. Uses gun powder."
i1.value = 135
i1.standard_rental_price = 18.75
i1.save()

i2=hmod.Item()
i2.name = "Waistcoat"
i2.description = "A replica of George Washington's waistcoat as he crossed the Delaware."
i2.value = 35
i2.standard_rental_price = 4.95
i2.save()


## Organizations:
org1 = hmod.Organization()
org1.given_name = "Colonial Heritage Foundation"
org1.organization_type = "Non-profit Organization"
org1.creation_date = "2007-01-09"
org1.save()

org2 = hmod.Organization()
org2.given_name = "Brigham Young University"
org2.organization_type = "Educational"
org2.creation_date = "2001-01-01"
org2.save()


## Areas:
area1 = hmod.Area()
area1.name = "Declaration Signing Room"
area1.description = "A display of the room that the Declaration of Independence was signed in."
area1.place_number = 1
area1.save()

## Events
event1 = hmod.Event()
event1.name = "Colonial Heritage Festival"
event1.start_date = "2015-06-29"
event1.end_date = "2015-07-11"
event1.map_file = "image.png"
event1.save()


## Rentals
rental = hmod.Rental()
rental.rental_time = "2015-02-21"
rental.due_date = "2015-03-04"
rental.save()

rental = hmod.Rental()
rental.rental_time = "2015-02-21"
rental.due_date = "2015-03-06"
rental.save()

rental = hmod.Rental()
rental.rental_time = "2015-02-21"
rental.due_date = "2015-03-17"
rental.save()


## Run the server
subprocess.call([sys.executable, "manage.py", "runserver"])



