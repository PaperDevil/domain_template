import sys
import logging

from loguru import logger

from app.external.logging.handlers import InterceptHandler


class LoguruLogger:

    @classmethod
    def make_logger(cls):
        return cls.customize()

    @classmethod
    def customize(cls):
        logger.remove()
        logger.add(sys.stdout, enqueue=True,
                   backtrace=True, level='INFO')
        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ['fastapi']:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]
        return logger.bind(request_id=None, method=None)
