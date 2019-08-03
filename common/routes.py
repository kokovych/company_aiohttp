from api import index, users_list
from aiohttp import web

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/api/user_list/', users_list)
