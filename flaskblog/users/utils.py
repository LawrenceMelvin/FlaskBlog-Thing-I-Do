from flask import url_for, current_app
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer

from flaskblog import mail


def send_confirmation_email(email):
    # This method can be used to send a confirmation email after registration
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = serializer.dumps(email, salt='email-confirm')
    confirm_url = url_for('users.confirm_email', token=token, _external=True)
    msg = Message('Confirm Your Email', recipients=[email])
    msg.body = f'Please confirm your email by clicking the link: {confirm_url}'
    mail.send(msg)
    return 'Confirmation email sent successfully!'

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