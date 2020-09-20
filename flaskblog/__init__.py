from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm



app = Flask(__name__)
app.config["SECRET_KEY"] = "SjG_2aPTAvf_VhRL-cWz2aObx8ylghvr"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db "
db = SQLAlchemy(app)