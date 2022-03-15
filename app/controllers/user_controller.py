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