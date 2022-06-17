from pydantic import Field

from app.internal.logic.entities.responses.base import Response


class ExceptionResponse(Response):
    detail: str = Field(..., example="Some message about mistake")
