from sqlalchemy import create_engine

from common.settings import config
from common.model import Base


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = Base.metadata
    meta.create_all(bind=engine)


def drop_tables(engine):
    meta = Base.metadata
    meta.drop_all(bind=engine)


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    create_tables(engine)
