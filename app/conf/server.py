from dataclasses import dataclass
from app.external.utils.config import ConfigUtils


@dataclass(frozen=True)
class ServerConfig:
    debug = ConfigUtils.env('DEBUG', bool, default=True)
    test_mode: bool = ConfigUtils.env('TEST_MODE', bool, default=False)
