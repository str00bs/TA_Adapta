"""File contains responses for the '/users' endpoint router"""

from api.schema.users import UsersList, UsersSchema
from fastapi import status

from .generic import GenericResponses


class UsersResponses:
    """Class contains users responses"""

    options = {
        status.HTTP_200_OK: {
            "content": None,
            "description": "Users router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Users router",
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
            "model": UsersSchema,
            "description": "Users successfully created",
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
            "model": UsersSchema,
            "description": "Users successfully retrieved",
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
            "model": UsersList,
            "description": "UsersList successfully retrieved",
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
            "model": UsersSchema,
            "description": "Users successfully updated",
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
            "model": UsersSchema,
            "description": "Users successfully replaced",
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
            "description": "Users successfully deleted",
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
