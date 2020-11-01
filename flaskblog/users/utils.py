import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
from flask_login import current_user
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_filename)
    
    #^ In the codes below We're gonna resize the picture to the 125*125
    output_size = (125, 125)
    image_file = Image.open(form_picture)
    image_file.thumbnail(output_size)
    
    image_file.save(picture_path)
    
    previous_picture = os.path.join(current_app.root_path, "static/profile_pics", current_user.image_file)
    if os.path.exists(previous_picture):
        os.remove(previous_picture)
    
    return picture_filename




def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender="khanjani1997@gmail.com", recipients=[user.email])
    
    
    
    msg.body = f"""Hey, To reset your password, Visit the following link:
    
{url_for("users.reset_token", token=token, _external = True)}
    
If you didn't make this request then ignore this email and no changes will be made
"""
    mail.send(msg)