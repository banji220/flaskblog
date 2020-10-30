from operator import methodcaller
import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from sqlalchemy.util.langhelpers import methods_equivalent
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, PasswordResetForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user,logout_user, login_required
from flask_mail import Message

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template("home.html", posts=posts)




@app.route("/about")
def about():
    return render_template("about.html", title = "About")















