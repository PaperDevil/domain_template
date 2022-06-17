from app.internal.web.http.exceptions import PersonExceptions
from app.schema.models import Person
from app.internal.logic.repos.person import PersonRepository
from app.internal.logic.services.base import Service


class PersonService(Service):
    @staticmethod
    async def create(person: Person) -> Person:
        return await PersonRepository().add(person)

    @staticmethod
    async def get_by_id(id: int) -> Person:
        person = await PersonRepository().get(id)
        if not person:
            raise PersonExceptions.NOT_FOUND
        return person

