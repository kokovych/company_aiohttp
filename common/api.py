from aiohttp import web
from sqlalchemy.sql import select, insert
from sqlalchemy import desc

from model import User
from validators import clean_create_user_data, validate_registration

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
        # cursor = await conn.execute(select([db.User]).where(db.User.id==1))
        cursor = await conn.execute(select([User]).order_by(desc('id')).limit(LIMIT_USERS_PER_REQUEST))
        result = await cursor.fetchall()
        for i in result:
            d = {}
            for key, value in i.items():
                d[key] = value
            data.append(d)
    return web.json_response(data)


async def create_user(request):
    resp = {'some': 'data'}
    user_data = await request.json()
    user_data = clean_create_user_data(user_data)
    try:
        async with request.app['db'].acquire() as conn:
            error = await validate_registration(conn, user_data)
            if error:
                ERROR_RESPONSE['error'] = error
                return web.json_response(ERROR_RESPONSE, status=400)
            await conn.execute(insert(User).values(user_data))

    except TypeError as err:
        ERROR_RESPONSE['error'] = str(err)
        return web.json_response(err, status=400)
    return web.json_response(resp)
