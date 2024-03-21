from flask import Flask

app = Flask(__name__)

@app.route('/homepage/', methods=["GET", "POST"])
def homepage():
    return "This is the homepage"

@app.route('/<int:number>/')
def incrementer(number):
    return f"Incremented number = {str(number + 1)}"

@app.route('/<string:name>/')
def print_name(name):
    return f"Your name is: {name}"

if __name__ == "__main__":
    app.run()
