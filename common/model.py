from sqlalchemy import (
    MetaData, Column, Integer, String, Sequence
)
from sqlalchemy.ext.declarative import declarative_base
# from passlib.hash import bcrypt

Base = declarative_base()
meta = MetaData()
USER_ID = Sequence('user_id_seq', start=1)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, USER_ID,  primary_key=True, server_default=USER_ID.next_value())
    username = Column(String(150), nullable=False)
    email = Column(String(300), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    first_name = Column(String(300), nullable=True)
    last_name = Column(String(300), nullable=True)

    def __init__(self, username, password, email):
        self.username = username
        # self.password = bcrypt.encrypt(password)
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)


def get_correct_fields():
    user_table_keys = User.__dict__.keys()
    results = list(filter(lambda x: not x.startswith('_'), user_table_keys))
    if 'id' in results:
        results.remove('id')
    return results
