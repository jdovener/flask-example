from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# config
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

from application import routes

