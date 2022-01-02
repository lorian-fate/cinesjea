from flask import Blueprint

global_access_bp = Blueprint('global_access', __name__, template_folder='templates')

from . import routes