from flask import Blueprint

account_bp = Blueprint('account', __name__, template_folder='templates')

from . import routes  # noqa: E402,F401
