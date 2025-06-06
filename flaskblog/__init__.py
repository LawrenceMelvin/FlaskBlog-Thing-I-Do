import os

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
load_dotenv()

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
#flask app run config
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY","default-secret")
# db init
# DATABASE_URL = os.getenv("FLASKBLOG_DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#hasing the password we are using flask_bcrypt
bcrypt = Bcrypt(app)
#flask-login init
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
#flask mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('FLASK_MAIL_USERNAME','default-user-name')
app.config['MAIL_PASSWORD'] = os.getenv('FLASK_MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('FLASK_MAIL_USERNAME','default-user-name')
mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)