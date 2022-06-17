import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    async def add(self, obj):
        ...

    @abc.abstractmethod
    async def get(self, id: int):
        ...
