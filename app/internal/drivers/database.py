import typing
from databases import Database


class AsyncDB:
    _database: typing.Optional[Database] = None

    @classmethod
    def setup_database(cls, connection_url: str) -> Database:
        if not cls._database:
            cls._database = Database(connection_url)
        return cls._database

    @classmethod
    async def start_connection(cls) -> None:
        assert cls._database
        if not cls._database.is_connected:
            await cls._database.connect()

    @classmethod
    async def close_connection(cls) -> None:
        assert cls._database
        if cls._database.is_connected:
            await cls._database.disconnect()
