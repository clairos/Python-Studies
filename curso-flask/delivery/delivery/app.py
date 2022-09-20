from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template(
            'index.html',
            name = request.args['name']
        )

    return app
