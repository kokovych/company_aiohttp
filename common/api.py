from aiohttp import web
import db
from db import User
from sqlalchemy.sql import select, insert
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from psycopg2 import errors

LIMIT_USERS_PER_REQUEST = 10

ERROR_RESPONSE = {
    'error': None
}


async def index(request):
    data = 'hello!'
    return web.json_response(data)

async def users_list(request):
    data = []
    async with request.app['db'].acquire() as conn:
        #cursor = await conn.execute(select([db.User]).where(db.User.id==1))
        cursor = await conn.execute(select([db.User]).order_by(desc('id')).limit(LIMIT_USERS_PER_REQUEST))
        result = await cursor.fetchall()
        for i in result:
            d = {}
            for key, value in i.items():
                d[key] = value
            data.append(d)
    return web.json_response(data)

async def create_user(request):
    resp = {'some': 'data'}
    data = await request.json()
    try:
        db.User(**data)
        async with request.app['db'].acquire() as conn:
            await conn.execute(insert(db.User).values(data))

    except errors.UniqueViolation as err:
        ERROR_RESPONSE['error'] = str(err)
        return web.json_response(ERROR_RESPONSE, status=400)

    except TypeError as err:
        ERROR_RESPONSE['error'] = str(err)
        return web.json_response(err, status=400)
    return web.json_response(resp)
