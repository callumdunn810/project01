from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField

app = Flask(__name__)

print('===========before forms====================')
class RequestForm(FlaskForm):
    brand = StringField('Brand:')
    film_name = StringField('Film Type:')
    exposure = StringField('Exposure:')
    price = StringField('Price:')
    quantity = StringField('Quantity:')
    submit = SubmitField('Make Order Request:')


class UpdateForm(FlaskForm):
    brand = StringField('Brand:')
    film_name = StringField('Film Type:')
    exposure = StringField('Exposure:')
    price = StringField('Price:')
    quantity = StringField('Quantity:')
    submit = SubmitField('Update order')

class StockForm(FlaskForm):
    stock_name = SelectField('Stock name', choices = [('Kodak'),('Fuji'),('Ilford')])
    submit = SubmitField('Search:')

class DeleteForm(FlaskForm):
    product_id = IntegerField('Order Number')
    submit = SubmitField('Delete Order')

    print('===========end forms====================')