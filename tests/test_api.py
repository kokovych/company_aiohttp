from aiohttp import web
import pytest

from common.db import init_pg, close_pg
from common.routes import setup_routes
from common.settings import test_config


@pytest.fixture()
async def setup_test_db():
    pass


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app['config'] = test_config
    setup_routes(app)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    return loop.run_until_complete(aiohttp_client(app))

# todo: create empty tables for test database


def foo():
    return 4


def test_foo_correct():
    assert foo() == 4


async def test_set_value(cli):
    resp = await cli.get('/')
    print(resp)
    assert resp.status == 200
