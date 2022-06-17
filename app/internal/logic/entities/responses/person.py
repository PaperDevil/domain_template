from pydantic import Field

from app.internal.logic.entities.frozens.name import Name
from app.internal.logic.entities.frozens.work import Work
from app.internal.logic.entities.responses.base import Response


class GetPersonResponse(Response):
    id: int = Field()
    name: Name
    work: Work
