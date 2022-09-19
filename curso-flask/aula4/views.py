# Extensão do Flask
from flask import Flask, request

def init_app(app): # callable function (padrao)
    """Inicialização de extensões"""
    
    @app.route("/") # VIEWS
    def index():
        print(request.args)
        return "Hello Clara!"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"