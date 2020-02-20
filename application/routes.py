from flask import Flask, render_template, url_for
from application import app
from application.models import Post

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

