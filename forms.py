from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)])
    
    email = StringField("Email", validators = [DataRequired(), Email()])
    
    password = PasswordField("Password", validators = [DataRequired()])
    
    confirm_password = PasswordField("Confirm Password", validations = [DataRequired(), EqualTo("password")])