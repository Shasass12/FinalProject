from flask import Blueprint, render_template, request, redirect, url_for, session

from interact_with_db import enter_sheelon2_row, enter_sheelon_row

sheelon2 = Blueprint('sheelon2', __name__, static_folder='static', static_url_path='/sheelon2',
                     template_folder='templates')


@sheelon2.route('/sheelon2')
def index():
    if request.args.get('msg'):
        return render_template('sheelon2.html', msg=request.args['msg'], key=request.args['key'])
    return render_template('sheelon2.html', key=request.args['key'])


@sheelon2.route('/sheelon2', methods=['POST'])
def send_sheelon_to_db():
    args = request.form
    enter_sheelon2_row(
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
    return redirect(url_for('sheelon3.index', key=request.args['key']))
