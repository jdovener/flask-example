from flask import Flask, render_template, url_for
from application import app

data = []

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=data)

@app.route('/about')
def about():
    return render_template("about.html")

