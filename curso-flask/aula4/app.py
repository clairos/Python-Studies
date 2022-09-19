import views
from flask import Flask, request


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    views.init_app(app)

    # with app.app_context(): ## usado para forçar um contexto
    # para imitar um request do usuário
    # usado para testes

    return app
