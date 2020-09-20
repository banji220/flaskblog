from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)], render_kw={"placeholder": "@username"})
    
    email = StringField("Email", validators = [DataRequired(), Email()], render_kw={"placeholder": "email@example.com"})
    
    password = PasswordField("Password", validators = [DataRequired()], render_kw={"placeholder": "Password must be between 4-20 character"})
    
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    
    submit = SubmitField("Sign Up")
    
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    
    password = PasswordField("Password", validators = [DataRequired()])
    
    remember_me = BooleanField("Remember Me")
    
    submit = SubmitField("Login")
    
    
    
    
