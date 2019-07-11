# aiohttpdemo_polls/db.py
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date,
)
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import bcrypt


Base = declarative_base()
meta = MetaData()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150),)
    email = Column(String(300), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    first_name = Column(String(300), nullable=False)
    last_name = Column(String(300), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = bcrypt.encrypt(password)
        self.email = email

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)

