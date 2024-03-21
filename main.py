from flask import Flask

app = Flask(__name__)

@app.route('/homepage/', methods=["GET", "POST"])
def homepage():
    return "This is the homepage"

if __name__ == "__main__":
    app.run()
