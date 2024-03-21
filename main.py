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

if __name__ == "__main__":
    app.run()
