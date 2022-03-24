from flask import Blueprint, render_template

home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')


@home.route('/')
def index():
    return render_template('home.html')
