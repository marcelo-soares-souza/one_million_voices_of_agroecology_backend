import os

from flask import Flask

from omv.db import db
from omv.jwt import jwt

from omv.routes.auth import bp as auth_bp
from omv.routes.locations import bp as locations_bp
from omv.routes.practices import bp as practices_bp

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['DEBUG'] = False
    app.config['TESTING'] = False
    app.config['CSRF_ENABLED'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL_OMV']
    app.config['SECRET_KEY'] = os.environ['DATABASE_URL_OMV_SECRET_KEY']
    app.config['JWT_SECRET_KEY'] = os.environ['DATABASE_URL_OMV_JWT_SECRET_KEY']

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    app.register_blueprint(locations_bp, url_prefix='/api/v1')
    app.register_blueprint(practices_bp, url_prefix='/api/v1')

    return app