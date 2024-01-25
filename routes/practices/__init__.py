from flask import Blueprint

bp = Blueprint('practices', __name__,)

from omv.routes.practices import routes
