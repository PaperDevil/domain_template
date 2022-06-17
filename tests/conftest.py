import typing
import sqlite3
import pytest

from fastapi.testclient import TestClient
from sqlalchemy.engine import create_engine

from app import ServerDriver
from app.internal.web.http.routes import general_router
from app.conf.database import get_db_url
from app.schema.base import metadata


@pytest.fixture(scope='session')
def client() -> typing.Generator:
    app = ServerDriver.create_app(
        debug=True, routers=[general_router],
        database_url=get_db_url()
    )
    metadata.create_all(create_engine(get_db_url()))
    with TestClient(app) as client:
        yield client


@pytest.fixture()
def session() -> typing.Generator:
    conn = sqlite3.connect(
        get_db_url().split('///')[1]
    )

    yield conn.cursor()

    conn.commit()
    conn.close()
