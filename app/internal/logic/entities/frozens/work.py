import typing
from app.internal.logic.entities.frozens.base import FrozenModel


class Work(FrozenModel):
    company: typing.Optional[str]
    position: typing.Optional[str]
