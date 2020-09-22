from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config["SECRET_KEY"] = "SjG_2aPTAvf_VhRL-cWz2aObx8ylghvr"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db "
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from flaskblog import routes

