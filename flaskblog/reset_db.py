from flask.cli import with_appcontext
import click

from flaskblog import db, app

# cmd -- flask --app reset_db.py reset-db
#flask --app <filename> <method>
@click.command('reset-db')
@with_appcontext
def reset_db():
    """Drop all tables and recreate them."""
    try:
        db.drop_all()  # Drop all tables
        db.create_all()  # Recreate all tables
        click.echo("Database has been reset successfully!")
    except Exception as e:
        click.echo(f"Error resetting the database: {e}")

# Register the CLI command
app.cli.add_command(reset_db)

