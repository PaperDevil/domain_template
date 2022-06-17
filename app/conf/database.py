from dataclasses import dataclass

from app.conf.server import ServerConfig
from app.external.utils.config import ConfigUtils


@dataclass(frozen=True)
class DatabaseConfig:
    engine: str = ConfigUtils.env('DB_ENGINE', str, default='postgresql')
    user: str = ConfigUtils.env('DB_USER', str, default='postgres')
    password: str = ConfigUtils.env('DB_PASSWORD', str, default='postgres')
    host: str = ConfigUtils.env('DB_HOST', str, default='localhost')
    port: str = ConfigUtils.env('DB_PORT', str, default=5432)
    database: str = ConfigUtils.env('DB_NAME', str, default='postgres')


@dataclass(frozen=True)
class DatabaseTestConfig:
    engine: str = "sqlite"
    database: str = "test_db.sqlite"


def get_db_url() -> str:
    if ServerConfig.test_mode:
        cfg = DatabaseTestConfig
        db_str = f"{cfg.engine}:///{cfg.database}"
    else:
        cfg = DatabaseConfig
        db_str = f"{cfg.engine}://{cfg.user}:{cfg.password}@{cfg.host}:{cfg.port}/{cfg.database}"

    return db_str
