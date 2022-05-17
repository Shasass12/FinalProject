from flask import Blueprint, render_template, request, redirect, url_for, session

from interact_with_db import enter_sheelon2_row, enter_sheelon3_row, enter_sheelon_row, update_used_key

sheelon3 = Blueprint('sheelon3', __name__, static_folder='static', static_url_path='/sheelon3',
                     template_folder='templates')


@sheelon3.route('/sheelon3')
def index():
    if request.args.get('msg'):
        return render_template('sheelon3.html', msg=request.args['msg'])
    return render_template('sheelon3.html')


@sheelon3.route('/sheelon3', methods=['POST', 'GET'])
def send_sheelon_to_db():
    args = request.form
    # if session and session['key'] and session['key'] != 'TEST-DESKTOP' and session['key'] != 'TEST-MOBILE':
    # sheelon = session['sheelon']
    # sheelon2 = session['sheelon2']
    sheelon = session.pop('sheelon')
    sheelon2 = session.pop('sheelon2')
    key = session.pop('key')
    enter_sheelon_row(
        sheelon['quest1'],
        sheelon['quest2'],
        sheelon['quest3'],
        sheelon['quest4'],
        sheelon['quest5'],
        sheelon['quest6'],
        sheelon['quest7'],
        sheelon['quest8'],
        key
    )
    enter_sheelon2_row(
        sheelon2['quest1'],
        sheelon2['quest2'],
        sheelon2['quest3'],
        sheelon2['quest4'],
        sheelon2['quest5'],
        sheelon2['quest6'],
        sheelon2['quest7'],
        sheelon2['quest8'],
        key
    )
    enter_sheelon3_row(
        args.get('quest1'),
        args.get('quest2'),
        args.get('quest3'),
        args.get('quest5'),
        args.get('quest6'),
        args.get('quest7'),
        args.get('quest8'),
        args.get('quest9'),
        args.get('quest10'),
        args.get('quest11'),
        args.get('quest12'),
        key
    )
    update_used_key(key)
    session.clear()

    return redirect(url_for('sheelon3.index', msg='תודה רבה על ההשתתפות בניסוי'))
