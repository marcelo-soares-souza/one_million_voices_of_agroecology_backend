import bcrypt

from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from omv.routes.auth import bp
from omv.models.accounts import Accounts

@bp.route("/login", methods=["POST"])
def login():
    
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    account = Accounts.query.filter_by(email=email).first()

    if account:
        salt = account.encrypted_password[:29]

        hashed_password = bcrypt.hashpw(str.encode(password), str.encode(salt))

        if email == account.email and hashed_password == str.encode(account.encrypted_password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token)
        
    return jsonify({"msg": "Bad username or password"}), 401

@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
