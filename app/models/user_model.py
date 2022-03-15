from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash

from app.configs.database import db


@dataclass
class UserModel(db.Model):
    id: str
    name: str
    last_name:str
    email: str

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(511), nullable=False)

    @property
    def password(self):
        return AttributeError("Password is not acessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)