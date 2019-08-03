from aiohttp import web
import db
from sqlalchemy.sql import select
from sqlalchemy import desc

LIMIT_USERS_PER_REQUEST = 10


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
    data = {'some': 'data'}
    return web.json_response(data)