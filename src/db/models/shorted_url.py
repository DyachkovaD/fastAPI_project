from datetime import datetime

from sqlalchemy import String, Column, Integer, TIMESTAMP

from .base import Base


class ShortedUrl(Base):
    __tablename__ = "url"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    origin = Column(String(256))
    shorted_url = Column(String(256), unique=True, index=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(256), unique=True, nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(1024), nullable=False)
    salt = Column(String(1024), nullable=False, unique=True, index=True)
