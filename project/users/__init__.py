from flask import Blueprint, render_template, abort

users_blueprint = Blueprint('users', __name__, template_folder='templates')

from . import routes

@users_blueprint.errorhandler(403)
def page_forbidden(e):
    return render_template('users/403.html'), 403

@users_blueprint.route('/admin')
def admin():
    abort(403)