from application import db



print('============models import===================')
class Orders(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))


class Stock(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   manufacturer = db.Column(db.String(50), nullable=False)
   model = db.Column(db.String(50), nullable=False)
   exposure = db.Column(db.String(50), nullable=False)
   price = db.Column(db.String(50), nullable=False)
   quantity = db.Column(db.String(200), nullable=False)
   order = db.relationship('Orders', backref='stock')

# from application import routes


# obj = Table.query.filter_by(name=form.product_name.data).first()
# all_stock = Stock.query.all()
# all_stock = Stock.query.filter_by(in_stock).all()
# all_stock = Stock.query.filter_by(
# kodak_only = Stock.query.filter_by(manufacturer = 'Kodak').all()
# fuji_only = Stock.query.filter_by(manufacturer = 'Fuji').all()
# ilford_only = Stock.query.filter_by(manufacturer = 'Ilford').all()
