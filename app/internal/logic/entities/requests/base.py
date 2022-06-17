from pydantic import BaseModel


class Request(BaseModel):
    class Config:
        user_enum_values = True
