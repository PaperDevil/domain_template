from os import environ
from typing import Any
from dotenv import load_dotenv

load_dotenv()

class ConfigUtils:

    @staticmethod
    def convert(key: str, value: Any, env_type: type) -> Any:
        if env_type == str:
            return value
        elif env_type == bool:
            if value.lower() in ["1", "true", "yes", "y", "ok", "on"]:
                return True
            if value.lower() in ["0", "false", "no", "n", "nok", "off"]:
                return False
            raise ValueError(
                "Invalid environment variable '%s' (expected a boolean): '%s'" % (key, value)
            )
        elif env_type == int:
            try:
                return int(value)
            except ValueError:
                raise ValueError("Invalid environment variable '%s' (expected an integer): '%s'" % (key, value))
        else:
            raise TypeError('Unknown type')

    @staticmethod
    def env(key: str, env_type: type, default: Any = None, required: bool = True):
        if key not in environ:
            if default is not None:
                return default
            if required:
                raise TypeError(f'Environment variable is absent {key}')
            return None

        return ConfigUtils.convert(key, environ[key], env_type)
