from aiohttp import web

async def index(request):
    data = {'some': 'data'}
    return web.json_response(data)
