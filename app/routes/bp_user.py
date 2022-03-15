from flask import Blueprint

from app.controllers import user_controller

bp = Blueprint("bp_user", __name__, url_prefix="/users")

bp.post("/signup")(user_controller.create_user)
bp.post("/signin")(user_controller.login_user)

bp.get("/profile")(user_controller.get_user)
bp.get("")(user_controller.get_all_users)

bp.patch("/profile")(user_controller.update_user)

bp.delete("/profile")(user_controller.delete_user)