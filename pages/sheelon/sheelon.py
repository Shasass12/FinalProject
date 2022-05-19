import time

from flask import Blueprint, render_template, request, redirect, url_for, session
from threading import Timer
from interact_with_db import enter_sheelon_row

sheelon = Blueprint('sheelon', __name__, static_folder='static', static_url_path='/sheelon',
                    template_folder='templates')

a = 0

@sheelon.route('/sheelon')
def index():
    return render_template('sheelon.html', key=request.args['key'])


@sheelon.route('/sheelon', methods=['POST'])
def send_sheelon_to_db():
    args = request.form

    enter_sheelon_row(
        args.get('quest1'),
        args.get('quest2'),
        args.get('quest3'),
        args.get('quest4'),
        args.get('quest5'),
        args.get('quest6'),
        args.get('quest7'),
        args.get('quest8'),
        request.args['key'],
    tmp=True
    )
    global a
    t = Timer(5.0, waitfunc)
    t.start()

    while(a!=1):
        time.sleep(1)
    a = 0
    return redirect(url_for('recommendation.index', favourite_food_style=args['quest7'], key=request.args['key']))


def waitfunc():
    global a
    a = 1