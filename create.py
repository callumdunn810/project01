from application import db
from application.models import Orders, Stock

db.drop_all()
db.create_all()


p1 = Stock(manufacturer = 'Kodak', model = 'Portra', exposure = '400', price = '15', quantity = '142')
p2 = Stock(manufacturer = 'Kodak', model = 'Ektar', exposure = '100', price = '10', quantity = '123')
p3 = Stock(manufacturer = 'Kodak', model = 'ColourPlus', exposure = '200', price = '6', quantity = '53')
p4 = Stock(manufacturer = 'Fuji', model = 'X-TRA', exposure = '400', price = '15', quantity = '34')
p5 = Stock(manufacturer = 'Fuji', model = 'Colour', exposure = '200', price = '6', quantity = '11')
p6 = Stock(manufacturer = 'Fuji', model = 'Provia', exposure = '100', price = '20', quantity = '94')
p7 = Stock(manufacturer = 'Ilford', model = 'HP-5', exposure = '400', price = '4', quantity = '35')
p8 = Stock(manufacturer = 'Ilford', model = 'Delta', exposure = '100', price = '7', quantity = '175')
p9 = Stock(manufacturer = 'Ilford', model = 'SFX', exposure = '200', price = '12', quantity = '12')
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.add(p7)
db.session.add(p7)
db.session.add(p8)
db.session.add(p9)
db.session.commit()
