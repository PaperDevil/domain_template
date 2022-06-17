from pydantic.main import BaseModel


class FrozenModel(BaseModel):
    class Config:
        frozen = True
