import typing

from app.internal.logic.repos.base import AbstractRepository
from app.schema.models import Person


class PersonRepository(AbstractRepository):

    async def add(self, obj: Person):
        return await obj.save()

    async def get(self, id: int) -> typing.Optional[Person]:
        return await Person.objects.get_or_none(id=id)


class PersonFakeRepository(AbstractRepository):

    datas = []

    async def add(self, obj):
        self.datas.append(obj)
        obj.id = len(self.datas) - 1
        return obj

    async def get(self, id: int):
        return self.datas[id] if id in self.datas else None
