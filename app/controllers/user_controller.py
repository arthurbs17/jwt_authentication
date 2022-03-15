from http import HTTPStatus

from flask import request, jsonify, current_app, session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.user_model import UserModel
from app.services.user_services import check_keys, check_values_types
from app.exc.invalids_requests import InvalidKeys, InvalidValues


@jwt_required()
def get_user():
    user = get_jwt_identity()

    return jsonify(user), HTTPStatus.OK


@jwt_required()
def update_user():
    session: Session = current_app.db.session

    try:
        data = request.get_json()
        check_values_types(data)

        decoded_user = get_jwt_identity()
        user: UserModel = UserModel.query.filter_by(email=decoded_user["email"]).first()

        for key, value in data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()

        return jsonify(user), HTTPStatus.OK
    
    except InvalidValues as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_user():
    session: Session = current_app.db.session
   
    decoded_user = get_jwt_identity()
    user: UserModel = UserModel.query.filter_by(email=decoded_user["email"]).first()

    session.delete(user)
    session.commit()

    return jsonify({"msg": f'User {user.name} has been deleted'}), HTTPStatus.OK


def create_user():
    session: Session = current_app.db.session

    try:
        data = request.get_json()
        check_keys(data)
        check_values_types(data)

        new_user = UserModel(**data)

        session.add(new_user)
        session.commit()

        return jsonify(new_user), HTTPStatus.CREATED
    
    except InvalidKeys as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
    
    except InvalidValues as error:
        return jsonify(error.message), HTTPStatus.BAD_REQUEST
    
    except IntegrityError:
        return {"error": "email already exists"}


def login_user():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data["email"]).first()

    if not user:
        return {"error": "user not found"}, HTTPStatus.NOT_FOUND
    
    if not user.check_password(data["password"]):
        return {"error": "email and password missmatch"}, HTTPStatus.UNAUTHORIZED
    
    token = create_access_token(user)

    return jsonify({"acess_token": token}), HTTPStatus.OK