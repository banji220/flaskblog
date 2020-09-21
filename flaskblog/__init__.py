from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config["SECRET_KEY"] = "SjG_2aPTAvf_VhRL-cWz2aObx8ylghvr"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db "
db = SQLAlchemy(app)