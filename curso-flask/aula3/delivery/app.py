from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Clara!</h1>"

@app.route("/sobre")
def sobre():
    return "<h1>Testando rota nova! (mais uma vez)</h1>"