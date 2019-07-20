"""
Think of main.py as the "brain" of our project. It tells our web app where to get information and resources which are
stored in the application structure.
"""

# Imports
import flask # Flask is a WGSI microframework for easy, lightweight, and scalable web applications.

app = flask.Flask(__name__) # Create the app object called "__name__"

"""
Flask apps begin in the root directory. They serve static HTML files in a directory called templates.
In order to create more pages for our web app, create a new HTML file in the templates folder.

Mess around with the files that are already inside the templates directory  to get a better understanding of how to
create web pages.
"""

"""
This is where we begin creating our Application Programming Interface (API).
 - An API allows you to request resources from a server using REST. You should look up REST if you're not familiar.
"""

@app.route('/', methods=["GET"])
def index():
    """
    -------------------------------------------  -------------------------------------------
    @app.route() is a decorator which changes the behavior of the index() function.
    @methods=["GET"] are the types of REST requests that the function takes. In this case, we only use GET which fetches resources.
     -------------------------------------------  -------------------------------------------
    @function index(): Renders index.html
    @params: none
    @returns: Renders index.html with two arguments for showing Jinja2 dynamic JavaScript.
    -------------------------------------------  -------------------------------------------
    """
    return flask.render_template('index.html', x=5, y=10)

@app.route('/problem1.html/', methods=["GET"])
def problem1():
    """
    @function problem1(): Renders problem1.html
    @params: none
    @returns: Renders problem1.html.
    -------------------------------------------  -------------------------------------------
    """
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