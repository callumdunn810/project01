from application import app, db
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from flask_sqlalchemy import SQLAlchemy
from application.forms import StockForm, RequestForm, DeleteForm, UpdateForm
from application.models import Stock


print('=========before routes ============')

###################################################### home #########################################################################


@app.route('/', methods=['GET', 'POST']) 
@app.route('/home', methods=['GET', 'POST']) 
def home():
    return render_template('home.html')

###################################################### about #########################################################################

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


###################################################### stock #########################################################################

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    error = ''
    form = StockForm()
    all_stock = Stock.query.all()
    kodak_only = Stock.query.filter_by(manufacturer = 'Kodak').all()
    fuji_only = Stock.query.filter_by(manufacturer = 'Fuji').all()
    ilford_only = Stock.query.filter_by(manufacturer = 'Ilford').all()

    stock_string = ''
    for  stock in all_stock:
        stock_string += "<br>" + "Brand:   " + str(stock.manufacturer) + "-" +  str(stock.model) + " " +  str(stock.exposure) + " " + " | " "£" + str(stock. price) + " " + " | " + " " + "On Hand:" + " " + str(stock.quantity)
    return render_template('stock.html', form=form) + stock_string



    
        
    return render_template('stock.html', form=form)



###################################################### order create #########################################################################

@app.route('/order-request', methods=['GET', 'POST'])
def add():
    error = ''
    form = RequestForm()

    if request.method == 'POST':
        brand = form.brand.data
        film_name = form.film_name.data
        exposure = form.exposure.data
        price = form.price.data
        quantity = form.quantity.data

        if len(brand) == 0 or len(film_name) == 0 or len(exposure) == 0 or (price) ==0 or (quantity) ==0:
            error = "*Please fill all fields*"
        else:
            new = Stock(manufacturer=form.brand.data, model=form.film_name.data, exposure=form.exposure.data, price=form.price.data, quantity=form.quantity.data)
            db.session.add(new)
            db.session.commit()
            return " Order submitted, We'll email you when it has been dispatched! "
    return render_template('request.html', form=form, message=error)


###################################################### order update #########################################################################

@app.route('/order-update', methods=['GET', 'POST', 'PUT'])
def update():
    error = ''
    form = UpdateForm()

    if request.method == 'PUT':
        brand = form.brand.data
        film_name = form.film_name.data
        exposure = form.exposure.data
        price = form.price.data
        quantity = form.quantity.data
        product_id = form.product_id.data

        if len(brand) == 0 or len(film_name) == 0 or len(exposure) == 0 or len(price) ==0 or len(quantity) ==0:
            error = "*Please fill all fields*"
            
        else:
            stock = Stock.query.filter_by(id=form.product_id.data).first()
            stock.brand = form.brand.data
            stock.film_name = form.film_name.data
            stock.exposure = form.exposure.data
            stock.price = form.price.data
            stock.quantity = form.quantity.data
            stock.product_id = form.product_id.data

            db.session.commit()
            return " Order submitted, We'll email you when it has been dispatched! "
    return render_template('update.html', form=form, message=error)


###################################################### order undo #########################################################################

@app.route('/order-undo', methods=['GET', 'POST', 'DELETE'])
def delete():
    error = ''
    form = DeleteForm()
    if request.method == 'DELETE':
        stock = Stock.query.get(form.product_id.data)
        db.session.remove(stock)
        db.session.commit()
    return render_template('undo.html', form=form)

print('=========end routes ============')