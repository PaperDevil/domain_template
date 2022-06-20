from loguru import logger
from fastapi import FastAPI
from fastapi.routing import APIRouter

from app.internal.drivers.database import AsyncDB


class ServerDriver:

    @staticmethod
    def create_app(
            debug: bool = True,
            routers: list[APIRouter] = None,
            database_url: str = None,
            log=None
    ) -> FastAPI:
        app = FastAPI(
            debug=debug
        )
        if log:
            app.logger = log
        else:
            app.logger = logger

        @app.on_event('startup')
        async def init():
            if database_url:
                AsyncDB.setup_database(database_url)
                await AsyncDB.start_connection()

        @app.on_event('shutdown')
        async def close():
            if database_url:
                await AsyncDB.close_connection()

        if routers:
            for router in routers:
                app.include_router(router)

        return app
