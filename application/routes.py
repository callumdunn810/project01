from application import app, db
from application.models import Stock

@app.route('/add')
def add():
    new_stock = Stock(name="New Film")
    db.session.add(new_stock)
    db.session.commit()
    return "Added new film to the request list"

@app.route('/serch')
def serch():
    all_stock = stock.query.all()
    stock_string = ""
    for stock in all_stock:
        stock_string += "<br>" + stock.name
    return stock_string

# @app.route('/update/<stock>')
# def update(stock):
