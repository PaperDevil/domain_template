import abc


class Service(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    async def create(obj):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    async def get_by_id(id: int):
        raise NotImplementedError
