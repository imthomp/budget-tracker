from flask import Blueprint

budget_bp = Blueprint('budget', __name__, template_folder='templates')

from . import routes
