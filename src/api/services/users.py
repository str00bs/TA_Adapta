"""File contains the UsersService class."""

from api.schema import UsersList, UsersSchema
from databases.models import UsersModel
from fastapi import status
from fastapi.exceptions import HTTPException
from masoniteorm.exceptions import QueryException


class UsersService:
    """Service class for the UsersRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: UsersSchema):
        """Creates a `UsersSchema` Entity from data"""
        try:
            secrets = data.get_secrets()
            data = data.model_dump()
            data.update(secrets)

            user = UsersModel.create(data).fresh()
        except QueryException as ex:
            status_code: int
            if "exists" in str(ex.args):
                status_code = 409
            else:
                status_code = 400

            raise HTTPException(
                status_code=status_code,
                detail=str(ex.args),
            )

        return UsersSchema(**user.serialize())

    def retrieve(self, uuid: str) -> UsersSchema:
        """Retrieves a `UsersSchema` Entity by uuid"""
        user = UsersModel.find(uuid)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return UsersSchema(**user.serialize())

    def listed(self, limit: int = 10, page_nr: int = 1, **kwargs) -> list[UsersSchema]:
        """Retrieves a `UsersSchema` Entity by uuid"""
        user = UsersModel.simple_paginate(limit, page_nr)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return UsersList(**user.serialize())

    def update(self, uuid: str, data: UsersSchema) -> UsersSchema:
        """Updates a `UsersSchema` Entity by uuid with data"""
        user = UsersModel.find(uuid)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            user.update(data)

        return UsersSchema(**user.serialize())

    def replace(self, uuid: str, data: UsersSchema) -> UsersSchema:
        """Replaces a `UsersSchema` Entity by uuid with data"""
        user = UsersModel.find(uuid)

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        try:
            self.delete(uuid)
            return self.create(data)
        except AttributeError:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

    def delete(self, uuid: str) -> None:
        """Delete a `UsersSchema` Entity by uuid"""
        user = UsersModel.find(uuid)
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            user.delete()

    def deleted(self, limit: int = 10, page_nr: int = 1) -> list[UsersSchema]:
        user = UsersModel.only_trashed().simple_paginate(limit, page_nr)
        return UsersList(**user.serialize())
