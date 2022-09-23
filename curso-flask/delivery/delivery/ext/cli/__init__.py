import click
from delivery.ext.db import db
from delivery.ext.site import models #noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        # este comando inicializa o banco de dados
        db.create_all()
    
    @app.cli.command()
    def list_orders():
        click.echo("list orders")

    @app.cli.command()
    def list_users():
        click.echo("list users")
