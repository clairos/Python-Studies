

@app.route("/") # VIEWS
def index():
    return "Hello Clara!"

@app.route("/contato")
def contato():
    return "<form><input type='text'></input></form>"