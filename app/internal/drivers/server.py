from loguru import logger
from fastapi import FastAPI
from fastapi.routing import APIRouter

from app.internal.drivers.database import AsyncPg


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
        async def init_primary_db():
            app.state.database = await AsyncPg.init_primary_db()
            # await CacheDriver.init_redis_connection(REDIS_HOST, REDIS_PORT, REDIS_PASSWORD)

        @app.on_event('shutdown')
        async def close_primary_db():
            await AsyncPg.close_primary_pool_db()
            # await CacheDriver.close_redis_connection()

        if routers:
            for router in routers:
                app.include_router(router)

        return app
