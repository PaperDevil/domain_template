from fastapi.routing import APIRouter

from app.internal.logic.entities.requests.person import AddPersonRequest
from app.internal.logic.entities.responses.base_exception import ExceptionResponse
from app.internal.logic.entities.responses.person import GetPersonResponse
from app.internal.logic.services.person import PersonService

general_router = APIRouter(responses={
    400: {'model': ExceptionResponse},
    500: {'model': ExceptionResponse}
})


@general_router.get('/hello')
async def hello_world():
    return "Hello World"


@general_router.post('/person', response_model=GetPersonResponse)
async def create_person(request: AddPersonRequest):
    person = await PersonService.create(request.to_person())
    return GetPersonResponse(
        id=person.id, name=person.name, work=person.work
    )


@general_router.get('/person/{id}', response_model=GetPersonResponse)
async def get_person(id: int):
    person = await PersonService.get_by_id(id)
    return GetPersonResponse(
        id=person.id, name=person.name, work=person.work
    )
