from logging import PlaceHolder
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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
    
    
    
    
class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder":"@username"})
    
    email = StringField("Email", validators = [DataRequired(), Email()], render_kw ={"placeholder":"email@example.com"})
    
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    
    submit = SubmitField("Update")
    
    def validate_username(self, username):
        #^ if username.data != current_username means that if they are equal it won't check the second validation, so if they are --->
        #^ ---> Equal it will check the second if statement and if it's True, it will throw an error!(So user can submit it's username without changing)
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                return ValidationError("That username is already taken, Please choose a different username.")
        
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                return ValidationError("That email is already taken!")
            
    

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")
    
    
    
    
class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"placeholder":"mail@example.com"})
    submit = SubmitField("Request Password Reset")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email, You must register first!")