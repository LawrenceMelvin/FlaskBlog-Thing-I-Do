# CLI Command to Insert Data
import click
from flask.cli import with_appcontext
from flaskblog import db, app
from flaskblog.models import User, Post

#flask --app testing.py add-user "lawrence" "lawrence@gamil.com" "post_title" "post_contetnt" "password"
#flask --app <filename> <method> <arguments>
@click.command('add-user')
@click.argument('username')
@click.argument('email')
@click.argument('post_title')
@click.argument('post_content')
@click.argument('password')
@with_appcontext
def add_user(username, email, post_title, post_content, password):
    """Insert a user and a post into the database."""
    user = User(username=username,email=email, password=password)
    post = Post(title=post_title, content=post_content, author=user)

    db.session.add(user)
    db.session.add(post)
    db.session.commit()
    click.echo(f"User '{username}' and their post '{post_title}' added successfully!")


# Register the CLI command
app.cli.add_command(add_user)