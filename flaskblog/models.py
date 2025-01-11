from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from itsdangerous import URLSafeTimedSerializer as Serializer
from datetime import datetime
from flaskblog import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username : Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password : Mapped[str] = mapped_column(nullable=False)
    # Relationship to Post table
    posts: Mapped[List["Post"]] = relationship("Post", back_populates="author",cascade='all, delete')

    def get_reset_token(self):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id':self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User({self.username},{self.email})"

class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    blog_posted: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.now())
    content: Mapped[str] = mapped_column(nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Relationship back to User table
    author: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"Post('{self.title}','{self.blog_posted}')"

