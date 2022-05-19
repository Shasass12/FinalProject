from flask import Blueprint, render_template, request

start = Blueprint('start', __name__, static_folder='static', static_url_path='/start', template_folder='templates')


@start.route('/start')
def index():
    return render_template('start.html', key=request.args['key'])
