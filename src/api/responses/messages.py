"""File contains responses for the '/messages' endpoint router"""

from api.schema.messages import MessagesList, MessagesSchema
from fastapi import status

from .generic import GenericResponses


class MessagesResponses:
    """Class contains messages responses"""

    options = {
        status.HTTP_200_OK: {
            "content": None,
            "description": "Messages router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Messages router",
                    "type": "string",
                }
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    # ? CRUD responses
    create = {
        status.HTTP_201_CREATED: {
            "model": MessagesSchema,
            "description": "Messages successfully created",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.bad_request,
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
        **GenericResponses.conflict,
    }

    retrieve = {
        status.HTTP_200_OK: {
            "model": MessagesSchema,
            "description": "Messages successfully retrieved",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.bad_request,
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    listed = {
        status.HTTP_200_OK: {
            "model": MessagesList,
            "description": "MessagesList successfully retrieved",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.bad_request,
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    update = {
        status.HTTP_200_OK: {
            "model": MessagesSchema,
            "description": "Messages successfully updated",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.bad_request,
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    replace = {
        status.HTTP_200_OK: {
            "model": MessagesSchema,
            "description": "Messages successfully replaced",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.bad_request,
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    delete = {
        status.HTTP_204_NO_CONTENT: {
            "content": None,
            "description": "Messages successfully deleted",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.bad_request,
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
