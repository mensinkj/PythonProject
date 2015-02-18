import homepage.models as hmod

## Products:
p1=hmod.Product()
p1.name = "Minted Coin"
p1.description = "Metal coin replica of olonial money. Has Colonial Heritage Foundation logo on it."
p1.category = "Mass Produced"
p1.current_price = 3.99
p1.save()


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

## Users
u1 = hmod.User()
u1.username = "jricks92"
u1.first_name = "Jameson"
u1.last_name = "Ricks"
u1.email = "jameson@glenricks.com"
u1.save()

u2 = hmod.User()
u2.username = "rnichols"
u2.first_name = "Rebecca"
u2.last_name = "Nichols"
u2.email = "rebeccaclogs@hotmail.com"
u2.save()

u3 = hmod.User()
u3.username = "rpehrson"
u3.first_name = "Ryan"
u3.last_name = "Person"
u3.email = "ryanpehrson@gmail.com"
u3.save()

u4 = hmod.User()
u4.username = "mensinkj"
u4.first_name = "Josh"
u4.last_name = "Mensink"
u4.email = "joshua@mensink.name"
u4.save()


## Organizations:
org1 = hmod.Organization()
org1.given_name = "Colonial Heritage Foundation"
org1.organization_type = "Non-profit Organization"
org1.creation_date = "2007-01-09"
org1.save()


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




