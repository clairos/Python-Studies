import click
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.db import models #noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        # este comando inicializa o banco de dados
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--password", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, password, admin):
        # adiciona novo usuario
        user = User(
            email=email,
            password=password,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo("New user was successfully added!")


    @app.cli.command()
    def list_orders():
        click.echo("list orders")

    @app.cli.command()
    def list_users():
        users = User.query.all()
        click.echo(f"users list: {users}")
