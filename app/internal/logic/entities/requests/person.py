from pydantic import Field

from app.internal.logic.entities.frozens.name import Name
from app.internal.logic.entities.requests.base import Request
from app.schema.models import Person


class AddPersonRequest(Request):
    first_name: str = Field(..., example='Ivan')
    last_name: str = Field(..., example='Ivanov')

    @property
    def name(self) -> Name:
        return Name(first=self.first_name, last=self.last_name)

    def to_person(self) -> Person:
        return Person(
            first_name=self.first_name,
            last_name=self.last_name
        )
