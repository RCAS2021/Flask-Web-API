from flask import Blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route('/hello/')
def hello():
    return "This is the homepage"
