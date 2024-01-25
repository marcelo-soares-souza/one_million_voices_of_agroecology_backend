from flask import Blueprint

bp = Blueprint('auth', __name__,)

from omv.routes.auth import routes