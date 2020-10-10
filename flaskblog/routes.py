from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user,logout_user, login_required

posts = [
    {
        "author": "@Banji",
        "title": "Blog Post 1",
        "content": "My first blog post in Flask",
        "date" : "Sep 1, 2020"
    },
    {
        "author": "@Amirdarx",
        "title": "Blog Post 2",
        "content": "My Second blog post in Flask",
        "date": "Sep 4, 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title = "About")


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account has been created for with ❤️! You are now be able to log in", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title = "Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            password_checking = bcrypt.check_password_hash(user.password, form.password.data)
            if user and password_checking:
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get("next")
                return redirect(next_page) if next_page else redirect(url_for("home"))
            else:
                 flash(f"Login Was Unsuccessful 😕, Please check your username and password!", "danger")
        
    return render_template("login.html", title = "Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("home"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title = "Account", image_file=image_file, form=form)