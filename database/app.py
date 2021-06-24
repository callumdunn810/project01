from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getnv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = geten('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = flask101
db = SQLAlchemy(app)


class Orders(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   quantity = db.Column(db.String(200), nullable=False)
   stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))


class Stock(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   manufacturer = db.Column(db.String(30), nullable=False)
   model = db.Column(db.String(30), nullable=False)
   exposure = db.Column(db.Integer, nullable=False)
   price = db.Column(db.Integer, nullable=False)
   in_stock = db.Column(db.String(30), nullable=False)
   order = db.relationship('Orders', backref='stock')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')