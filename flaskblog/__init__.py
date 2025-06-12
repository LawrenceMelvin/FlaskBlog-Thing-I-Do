import os
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

# Custom SQLAlchemy base class
class Base(DeclarativeBase):
    pass

# Flask app setup
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database URL (without ?ssl=true)
db_url = os.getenv("FLASKBLOG_DATABASE_URL")

# Aiven SSL configuration
ssl_args = {
    "ssl": {
        "ca": os.path.join("certs", "ca.pem")
    }
}

# Create SQLAlchemy engine manually
engine = create_engine(db_url, connect_args=ssl_args)

# Create SQLAlchemy session manually
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Attach SQLAlchemy to app
db = SQLAlchemy(model_class=Base)
db.session = Session  # manually assign session
app.config['SQLALCHEMY_DATABASE_URI'] = db_url  # required for Flask-SQLAlchemy
db.init_app(app)

# Bcrypt setup
bcrypt = Bcrypt(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('FLASK_MAIL_USERNAME', 'default-user-name')
app.config['MAIL_PASSWORD'] = os.getenv('FLASK_MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('FLASK_MAIL_USERNAME', 'default-user-name')
mail = Mail(app)

# Register Blueprints
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
