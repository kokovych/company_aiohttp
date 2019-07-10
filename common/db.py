# aiohttpdemo_polls/db.py
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

question = Table(
    'user', meta,

    Column('id', Integer, primary_key=True),
    Column('username', String(200), nullable=False),
    Column('password', String(200), nullable=False),
    Column('email', String(256), nullable=False),
    Column('first_name', String(256), nullable=True),
    Column('last_name', String(256), nullable=True),
    Column('registration_date', Date, nullable=False),
    Column('role', Integer, nullable=False),
)

