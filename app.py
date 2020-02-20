from flask import Flask, render_template, url_for

app = Flask(__name__)

data = []
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=data)

@app.route('/about')
def about():
    return render_template("about.html")
