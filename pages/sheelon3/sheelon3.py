from flask import Blueprint, render_template, request, redirect, url_for, session

from interact_with_db import enter_sheelon2_row, enter_sheelon3_row, enter_sheelon_row, update_used_key, get_sheelon

sheelon3 = Blueprint('sheelon3', __name__, static_folder='static', static_url_path='/sheelon3',
                     template_folder='templates')


@sheelon3.route('/sheelon3')
def index():
    if request.args.get('msg'):
        return render_template('sheelon3.html', msg=request.args['msg'], key=request.args['key'])
    return render_template('sheelon3.html', key=request.args['key'])


@sheelon3.route('/sheelon3', methods=['POST', 'GET'])
def send_sheelon_to_db():
    args = request.form
    sheelon = get_sheelon('sheelon_tmp', request.args['key'])
    sheelon2 = get_sheelon('sheelon2_tmp', request.args['key'])
    print(sheelon)
    enter_sheelon_row(
        sheelon[0][0],
        sheelon[0][1],
        sheelon[0][2],
        sheelon[0][3],
        sheelon[0][4],
        sheelon[0][5],
        sheelon[0][6],
        sheelon[0][7],
        request.args['key']
    )
    enter_sheelon2_row(
        sheelon2[0][0],
        sheelon2[0][1],
        sheelon2[0][2],
        sheelon2[0][3],
        sheelon2[0][4],
        sheelon2[0][5],
        sheelon2[0][6],
        sheelon2[0][7],
        request.args['key']
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
        request.args['key']
    )
    update_used_key(request.args['key'])
    session.clear()

    return redirect(url_for('thankyou.index', msg='תודה רבה על ההשתתפות בניסוי'))
