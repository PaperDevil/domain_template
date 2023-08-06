import uvicorn

from app import ServerDriver
from app.conf.server import ServerConfig
from app.internal.web.http.routes import general_router
from app.external.logging.custom import LoguruLogger

# Setup Application with own settings
app = ServerDriver.create_app(
    debug=ServerConfig.debug,
    routers=[general_router],
    log=LoguruLogger.make_logger()
)


if __name__ == '__main__':
    uvicorn.run('manage:app')
