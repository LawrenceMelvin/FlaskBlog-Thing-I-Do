from flask import url_for
from flask_mail import Message

from flaskblog import mail


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender='noreply@demo.com',
        recipients=[user.email],
        body=f'''To reset your password, visit the following:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made
'''
    )
    mail.send(msg)
    return 'Email sent succesfully!'