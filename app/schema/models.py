import ormar

from app.internal.logic.entities.frozens.name import Name
from app.internal.logic.entities.frozens.work import Work
from app.schema.base import BaseModel


class Person(BaseModel):
    class Meta(ormar.ModelMeta):
        tablename = "persons"
    first_name: str = ormar.String(max_length=128)
    last_name: str = ormar.String(max_length=128)
    work_company: str = ormar.String(max_length=128, nullable=True)
    work_position: str = ormar.String(max_length=128, nullable=True)

    @property
    def name(self) -> Name:
        return Name(first=self.first_name, last=self.last_name)

    @property
    def work(self) -> Work:
        return Work(company=self.work_company, position=self.work_position)
