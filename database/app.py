from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URI') 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
from my_project import routes


class Stock(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   manufacturer = db.Column(db.String(30), nullable=False)
   model = db.Column(db.String(30), nullable=False)
   exposure = db.Column(db.Integer, nullable=False)
   price = db.Column(db.Integer, nullable=False)

class Orders(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   in_stock = db.Column(db.boolean, nullable=False)
   quantity = db.Column(db.integer), nullable=False)
   Stock = db.relationship('Stock', backref='Orders')

if __name__ == "__main__":
    app.run(debug=True)