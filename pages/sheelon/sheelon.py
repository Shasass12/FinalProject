import time

from flask import Blueprint, render_template, request, redirect, url_for, session
from threading import Timer

sheelon = Blueprint('sheelon', __name__, static_folder='static', static_url_path='/sheelon',
                    template_folder='templates')

a = 0

@sheelon.route('/sheelon')
def index():
    return render_template('sheelon.html')


@sheelon.route('/sheelon', methods=['POST'])
def send_sheelon_to_db():
    args = request.form
    if session['key'] != 'TEST-DESKTOP' and session['key'] != 'TEST-MOBILE':
        session['sheelon'] = {
            'quest1': args.get('quest1'),
            'quest2': args.get('quest2'),
            'quest3': args.get('quest3'),
            'quest4': args.get('quest4'),
            'quest5': args.get('quest5'),
            'quest6': args.get('quest6'),
            'quest7': args.get('quest7'),
            'quest8': args.get('quest8'),
        }
    global a
    t = Timer(5.0, waitfunc)
    t.start()

    while(a!=1):
        time.sleep(1)
    a = 0
    return redirect(url_for('recommendation.index', favourite_food_style=args['quest7']))


def waitfunc():
    global a
    a = 1