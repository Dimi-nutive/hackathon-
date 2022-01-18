import flask

app = flask.Flask('__main__')

@app.route("/")
def lol():
    return "lol"

app.run()