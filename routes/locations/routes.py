from flask import jsonify
from flask_jwt_extended import jwt_required

from omv.routes.auth import bp
from omv.models.locations import Locations

@bp.route('/locations/')
@jwt_required()
def locations():
  try:
    locations = Locations.query.all()

    if locations:
      return jsonify(locations)
  except Exception as e:
    print(f'[locations] Error: {e}')
          
  return jsonify({ 'message': 'Locations not found'})

@bp.route('/locations/<id>')
@jwt_required()
def location(id):
  try:
    location = Locations.query.filter_by(id=id).first()

    if location:
      return jsonify(location)
  except Exception as e:
    print(f'[location] Error: {e}')
          
  return jsonify({ 'message': 'Location not found'})
