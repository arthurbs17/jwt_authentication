from flask import Flask

from app.routes.bp_api import bp as bp_api


def init_app(app: Flask):
    app.register_blueprint(bp_api)