from flask import jsonify
from flask_jwt_extended import jwt_required

from omv.routes.auth import bp
from omv.models.practices import Practices

@bp.route('/practices/')
@jwt_required()
def practices():
  practices = Practices.query.all()

  return jsonify(practices)
