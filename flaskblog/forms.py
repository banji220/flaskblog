from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)], render_kw={"placeholder": "@username"})
    
    email = StringField("Email", validators = [DataRequired(), Email()], render_kw={"placeholder": "email@example.com"})
    
    password = PasswordField("Password", validators = [DataRequired()], render_kw={"placeholder": "Password must be between 4-20 character"})
    
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    
    submit = SubmitField("Sign Up")
    
    #&The code below is like a template for validation error(SO remember how to use it)
    #!def validate_field(self, field):
        #!if True:
            #!raise ValidationError("Validation message")
    
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is already taken, Please choose a different username.")
    
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("That email is already taken!")
        

        
        
        
class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    
    password = PasswordField("Password", validators = [DataRequired()])
    
    remember_me = BooleanField("Remember Me")
    
    submit = SubmitField("Login")
    
    
    
    
