# Contextos

from distutils.log import debug
from flask import Flask
app = Flask(__name__)

## 1 Configuração
#- Add Configuração	
app.config["DEBUG"] = True 
app.config["SQLALCHEMY_DB_URI"] = "mysql://.." 

#- Registrar Rotas
@app.route("/path")
def funcao(): # callable
    ...

app.add_url_rule("/path", funcao)

#- Inicializar Extensões
from flask_admin import Admin
Admin.init_app(app)

#- Registrar Blueprints
app.register_blueprint(...)

#- Add Hooks
@app.before_request(...)
def funcao():
    ...

@app.error_handler(...)
def funcao():
    ...

#- Chamar outras Factories
# views.init_app(app)


## 2 App Context
### App está pronto! `app`
#- Testar
app.test_client
"""debug
objetos globais do Flask
(importar request, session, g)
- Hooks"""

from flask import current_app, g


## 3 Request Context
# Entra após o primeiro request, primeiro GET
# usar globais do flask
from flask import request, session 

request.args
request.form
