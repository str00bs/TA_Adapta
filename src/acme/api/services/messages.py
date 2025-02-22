"""File contains the MessagesService class."""

from api.schema import MessagesList, MessagesSchema
from databases.models import MessagesModel
from fastapi import status
from fastapi.exceptions import HTTPException
from masoniteorm.exceptions import QueryException


class MessagesService:
    """Service class for the MessagesRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: MessagesSchema):
        """Creates a `MessagesSchema` Entity from data"""
        try:
            message = MessagesModel.create(data.model_dump()).fresh()
        except QueryException as ex:
            if "exists" in str(ex.args):
                status_code = 409
            else:
                status_code = 400

            raise HTTPException(
                status_code=status_code,
                detail=str(ex.args).split("DETAIL")[0],
            )

        return MessagesSchema(**message.serialize())

    def retrieve(self, uuid: str) -> MessagesSchema:
        """Retrieves a `MessagesSchema` Entity by uuid"""
        message = MessagesModel.find(uuid)

        if not message:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return MessagesSchema(**message.serialize())

    def listed(
        self, limit: int = 10, page_nr: int = 1, **kwargs
    ) -> list[MessagesSchema]:
        """Retrieves a `MessagesSchema` Entity by uuid"""
        message = MessagesModel.simple_paginate(limit, page_nr)

        if not message:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return MessagesList(**message.serialize())

    def update(self, uuid: str, data: dict) -> MessagesSchema:
        """Updates a `MessagesSchema` Entity by uuid with data"""
        message = MessagesModel.find(uuid)

        if not message:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            message.update(data)

        return MessagesSchema(**message.serialize())

    def replace(self, uuid: str, data: MessagesSchema) -> MessagesSchema:
        """Replaces a `MessagesSchema` Entity by uuid with data"""
        message = MessagesModel.find(uuid)

        if not message:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        try:
            self.delete(uuid)
            return self.create(data)
        except AttributeError:
            raise HTTPException(status.HTTP_400_BAD_REQUEST)

    def delete(self, uuid: str) -> None:
        """Delete a `MessagesSchema` Entity by uuid"""
        message = MessagesModel.find(uuid)
        if not message:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            message.delete()

    def deleted(self, limit: int = 10, page_nr: int = 1) -> list[MessagesSchema]:
        message = MessagesModel.only_trashed().simple_paginate(limit, page_nr)
        return MessagesList(**message.serialize())
