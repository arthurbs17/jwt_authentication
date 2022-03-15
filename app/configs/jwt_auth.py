from environs import Env
from flask import Flask
from flask_jwt_extended import JWTManager


def init_app(app: Flask):
    env = Env()
    env.read_env()

    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")
    JWTManager(app)