from flask import Blueprint

from app.routes.bp_user import bp as bp_user


bp = Blueprint("bp_api", __name__, url_prefix="/api")

bp.register_blueprint(bp_user)