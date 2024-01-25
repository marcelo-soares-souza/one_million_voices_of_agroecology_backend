from flask import Blueprint

bp = Blueprint('locations', __name__,)

from omv.routes.locations import routes