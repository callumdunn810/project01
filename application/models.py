from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class Stock(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   manufacturer = db.Column(db.String(30), nullable=False)
   model = db.Column(db.String(30), nullable=False)
   exposure = db.Column(db.Integer, nullable=False)
   price = db.Column(db.Integer, nullable=False)
   in_stock = db.Column(db.String(30), nullable=False)