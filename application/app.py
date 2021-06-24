from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST']) 
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    return render_template('stock.html')


if __name__=="__main__":
    app.run(debug=True)
