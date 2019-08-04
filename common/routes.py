from api import index, users_list, create_user
from aiohttp import web

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/api/user_list/', users_list)
    app.router.add_post('/api/user/', create_user)
