import uvicorn

from app import ServerDriver
from app.conf.server import ServerConfig
from app.conf.database import get_db_url
from app.internal.web.http.routes import general_router

# Setup Application with own settings
app = ServerDriver.create_app(
    debug=ServerConfig.debug,
    # to run instantly try to use get_test_db_url
    database_url=get_db_url(),
    routers=[general_router]
)


if __name__ == '__main__':
    uvicorn.run('manage:app')
