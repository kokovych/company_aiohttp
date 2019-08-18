# aiohttpdemo_polls/db.py
import aiopg.sa
from sqlalchemy.sql.expression import select

from model import User


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


async def get_user_by_email(conn, email):
    cursor = await conn.execute(
        select([User]).where(User.email == email)
    )
    result = await cursor.fetchall()
    return result
