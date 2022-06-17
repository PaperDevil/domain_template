from app.internal.logic.entities.frozens.base import FrozenModel


class Name(FrozenModel):
    first: str
    last: str

    @property
    def full_name(self):
        return f"{self.first} {self.last}"
