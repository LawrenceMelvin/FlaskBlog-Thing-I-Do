from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
#flask app run config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ab95d4db05bb3c5f41359e52551cd52a'
# db init
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
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
app.config['MAIL_USERNAME'] = 'lawrenc2000april@gmail.com'
app.config['MAIL_PASSWORD'] = 'yqphaqiwvhqwcfow'
app.config['MAIL_DEFAULT_SENDER'] = 'lawrenc2000april@gmail.com'
mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)