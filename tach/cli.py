"""Command line interface."""
import click
from flask import current_app
from flask.cli import with_appcontext


@click.command()
@click.option('-o', '--output', default='erd.png', help='Output filename')
@with_appcontext
def erd(output):
    """Draw an entity relation diagram for the database."""
    import eralchemy
    eralchemy.render_er(current_app.extensions['sqlalchemy'].db.Model, output)
