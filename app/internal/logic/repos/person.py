import typing

from app.internal.logic.repos.base import AbstractRepository
from app.schema.models import Person


class PersonRepository(AbstractRepository):

    async def add(self, obj: Person) -> Person:
        person = await obj.save()
        return person

    async def get(self, id: int) -> typing.Optional[Person]:
        obj = await Person.objects.get_or_none(id=id)
        return obj
