from flask import Blueprint

global_users_bp = Blueprint('global_users', __name__, template_folder='templates')

from . import routes