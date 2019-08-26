from aiohttp import web
import pytest
from sqlalchemy import create_engine

from common.db import init_pg, close_pg
from common.routes import setup_routes
from common.settings import test_config
from init_db import create_tables, drop_tables, DSN


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app['config'] = test_config
    setup_routes(app)
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture()
def setup_test_db():
    db_url = DSN.format(**test_config['postgres'])
    engine = create_engine(db_url)
    create_tables(engine)


@pytest.fixture()
def drop_test_db():
    db_url = DSN.format(**test_config['postgres'])
    engine = create_engine(db_url)
    drop_tables(engine)
