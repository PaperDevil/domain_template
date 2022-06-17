from fastapi import HTTPException


class PersonExceptions:
    NOT_FOUND = HTTPException(status_code=404, detail="Person with this data not found")
