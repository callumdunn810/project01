from falsk import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Grg170dx@34.105.139.189:3306/projectdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.SQLAlchemy(app)

# class Products(FlaskForm):
#     brand = StringField('Brand :')
#     model = StringField('Type :')
#     exposure = StringField('Exposure :')
#     submit = SubmitField('Go!')





from application import routes
