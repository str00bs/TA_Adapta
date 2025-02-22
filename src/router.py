"""File contains API routers and endpoint controllers"""

import pathlib
import secrets
from uuid import UUID

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    Request,
    Security,
    status,
)
from fastapi.responses import Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from masoniteorm.exceptions import QueryException

from config import Config
from models import MessagesModel, UsersModel
from schema import MessagesList, MessagesSchema, UsersList, UsersSchema


# ? Setting up basic auth
def auth(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    """Basic Auth validation method against configured credentials"""
    valid_credentials = all(
        [
            secrets.compare_digest(
                credentials.username.encode("utf8"),
                Config.Auth.username.encode("utf8"),
            ),
            secrets.compare_digest(
                credentials.password.encode("utf8"),
                Config.Auth.password.encode("utf8"),
            ),
        ]
    )
    if not valid_credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


templates = Jinja2Templates(
    directory=pathlib.Path(__file__).parent.joinpath("frontend")
)


# ? Router Configuration
router = APIRouter(dependencies=[Security(auth)])


# ? Serving frontend
@router.get(path="/", operation_id="api.system.index", tags=["System"])
async def index(request: Request) -> Response:
    """Serves frontend template"""
    return templates.TemplateResponse(request, "index.html")


# ? User Routes
@router.options(path="/api", operation_id="api.users.options", tags=["User CRUD"])
async def users_options() -> Response:
    """Endpoint is used to find options for the `Users` router"""
    headers = ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]
    return Response(headers={"allow": str(headers)})


# ? CRUD Endpoints
@router.post(
    path="/users",
    operation_id="api.users.create",
    tags=["User CRUD"],
    status_code=201,
)
async def create_user(
    users: UsersSchema,
    background: BackgroundTasks,
) -> UsersSchema:
    """Endpoint is used to create a `Users` entity"""
    try:
        secrets = users.get_secrets()
        data = users.model_dump()
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


@router.get(path="/users/{uuid}", operation_id="api.users.retrieve", tags=["User CRUD"])
async def retrieve_user(
    uuid: UUID = Path(description="Unique Identifier for the Users Entity to retrieve"),
) -> UsersSchema:
    """Endpoint is used to retrieve a `Users` entity"""
    user = UsersModel.find(uuid)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return UsersSchema(**user.serialize())


@router.get(path="/users", operation_id="api.users.listed", tags=["User CRUD"])
async def retrieve_users_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
) -> UsersList:
    """Endpoint is used to retrieve a list of `Users` entities"""
    user = UsersModel.simple_paginate(limit, page_nr)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return UsersList(**user.serialize())


@router.patch(path="/users/{uuid}", operation_id="api.users.update", tags=["User CRUD"])
async def update_user(
    data: dict = Body(..., description="Key,value pairs to be updated"),
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to update"
    ),
) -> UsersSchema:
    """Endpoint is used to update a `Users` entity"""
    user = UsersModel.find(uuid)

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        user.update(data)

    return UsersSchema(**user.serialize())


@router.delete(
    path="/users/{uuid}",
    operation_id="api.users.delete",
    tags=["User CRUD"],
    status_code=204,
)
async def delete_user(
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to delete"
    )
) -> Response:
    """Endpoint is used to delete a `Users` entity"""
    user = UsersModel.find(uuid)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        user.delete()
        return Response(None, 204)


# ? Messages
@router.post(
    path="/messages", operation_id="api.messages.create", tags=["Messages CRUD"]
)
async def create_message(
    messages: MessagesSchema,
    background: BackgroundTasks,
) -> MessagesSchema:
    """Endpoint is used to create a `Messages` entity"""
    try:
        message = MessagesModel.create(messages.model_dump()).fresh()
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


@router.get(
    path="/messages/{uuid}",
    operation_id="api.messages.retrieve",
    tags=["Messages CRUD"],
)
async def retrieve_message(
    uuid: UUID = Path(
        description="Unique Identifier for the Messages Entity to retrieve"
    ),
) -> MessagesSchema:
    """Endpoint is used to retrieve a `Messages` entity"""
    message = MessagesModel.find(uuid)

    if not message:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return MessagesSchema(**message.serialize())


@router.get(
    path="/messages", operation_id="api.messages.listed", tags=["Messages CRUD"]
)
async def retrieve_messages_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
) -> MessagesList:
    """Endpoint is used to retrieve a list of `Messages` entities"""
    message = MessagesModel.simple_paginate(limit, page_nr)

    if not message:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return MessagesList(**message.serialize())


@router.patch(
    path="/messages/{uuid}", operation_id="api.messages.update", tags=["Messages CRUD"]
)
async def update_message(
    data: dict = Body(..., description="Key,value pairs to be updated"),
    uuid: str = Path(
        ..., description="Unique Identifier for the Messages Entity to update"
    ),
) -> MessagesSchema:
    """Endpoint is used to update a `Messages` entity"""
    message = MessagesModel.find(uuid)

    if not message:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        message.update(data)

    return MessagesSchema(**message.serialize())


@router.delete(
    path="/messages/{uuid}",
    operation_id="api.messages.delete",
    tags=["Messages CRUD"],
    status_code=204,
)
async def delete_message(
    uuid: str = Path(
        ..., description="Unique Identifier for the Messages Entity to delete"
    ),
) -> Response:
    """Endpoint is used to delete a `Messages` entity"""
    message = MessagesModel.find(uuid)
    if not message:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        message.delete()
        return Response(None, status_code=204)
