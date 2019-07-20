import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', x=5, y=10)

@app.route('/problem1.html/')
def problem1():
    return flask.render_template('problem1.html')

@app.after_request
def add_header(resp):
    """
    Prevent the browser from caching.
    """
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    resp.headers["Expires"] = "0"
    resp.headers["Pragma"] = "no-cache"
    return resp

if __name__ == "__main__":
    app.run(debug=False)