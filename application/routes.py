from flask import Flask, render_template, url_for, redirect
from application import app, db, bcrypt
from application.models import Post, User
from application.forms import PostForm, RegisterForm

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/create', methods=['GET', 'POST'])
def post_create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            first_name=form.first_name.data,
            last_name=form.last_name.data, title=form.title.data, content=form.content.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("post.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("register.html", form=form)

