from flask import Flask, jsonify, request
import werkzeug
from blueprints import home
from blueprints import contact

app = Flask(__name__)

app.register_blueprint(home.home_bp, url_prefix='/home')
app.register_blueprint(contact.contact_bp, url_prefix='/contact')

@app.route('/homepage/', methods=["GET", "POST"])
def homepage():
    return "This is the homepage"

# Examples url variables
@app.route('/<int:number>/')
def incrementer(number):
    return f"Incremented number = {str(number + 1)}"

@app.route('/<string:name>/')
def print_name(name):
    print(f"Request data: {request.data}")
    print(f"Parsed URL parameters: {request.args}")
    # This will return an unsupported media type error if not application/json
    print(f"Parsed json if mimetype = application/json: {request.json}")
    print(f"Form parameters: {request.form}")
    print(f"Combination args and form: {request.values}")
    print(f"All uploaded files: {request.files}")
    print(f"Authorization header: {request.authorization}")
    print(request.path)
    return f"Your name is: {name}"

# Examples jsonify
@app.route('/person/')
def jsonify_person():
    return jsonify({"name": "Pudha", "address": "Brazil"})

@app.route('/create_list/<int:number>/')
def jsonify_list(number):
    return jsonify(list(range(number)))

# Examples of automatic redirecting
# Will not redirect if it has the trailing slash "/"
# In this app, it will treat it as a normal string,
# calling the print_name method
@app.route('/redirect')
def redirect():
    return "Will not redirect"

# Will redirect if there isn't the trailing slash "/"
@app.route('/will_redirect/')
def will_redirect():
    return "Redirected"

# Status code examples
@app.route('/status_code/')
def status_code():
    return "The status code has changed from the default 200 to 418 (I'm a teapot)", 418

# Examples request

# Before request
@app.before_request
def before():
    # Pylint false-positive on method logger has no 'debug/info/warning/error' member
    app.logger.debug('This is a DEBUG message')
    app.logger.info('This is an INFO message')
    app.logger.warning('This is a WARNING message')
    app.logger.error('This is an ERROR message')
    print("This is executed before each request")

# After request
@app.after_request
def after(response):
    print(f"This is executed after each request, example: status code = {response.status_code}, status = {response.status}")
    print(f"Response data: {response.data}")
    return response

# Error handler example
@app.errorhandler(werkzeug.exceptions.UnsupportedMediaType)
def handle_unsupported_media_type(e):
    return "There was an error with the media type!"


if __name__ == "__main__":
    # debug = True, server will reload when code changes
    app.run(debug=True)

    # use_reloader = True, servr will restart when code changes
    #app.run(use_reloader=True)

    # threaded = True, the process will handle each request in a separated thead
    #app.run(threaded=True)

    # ssl_context = ssl.SSLContext, a tuple in the form(cert_file, key_file),
    # or 'adhoc' if the server should create automatically the context,
    # Requires criptography library
    # SSL Context for the connection, used to host the flask application on https instead of http
    #app.run(ssl_context='adhoc')

    #app.run()
