from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/homepage/', methods=["GET", "POST"])
def homepage():
    return "This is the homepage"

# Examples url variables
@app.route('/<int:number>/')
def incrementer(number):
    return f"Incremented number = {str(number + 1)}"

@app.route('/<string:name>/')
def print_name(name):
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
if __name__ == "__main__":
    app.run()
