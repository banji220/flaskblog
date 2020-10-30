from logging import PlaceHolder
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User





    

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



class PasswordResetForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password must be between 4-20 character"})
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")] )
    submit = SubmitField("Reset Password")