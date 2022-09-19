# Extensão do Flask

def init_app(app): # callable function (padrao)
    """Inicialização de extensões"""
    
    @app.route("/") # VIEWS
    def index():
        return "Hello Clara!"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"