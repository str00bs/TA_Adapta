"""File contains router for '/messages' CRUD endpoints"""

from uuid import UUID

from api.auth import Auth
from api.responses import MessagesResponses
from api.schema import MessagesList, MessagesSchema
from api.services import MessagesService
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    Depends,
    Path,
    Query,
    Security,
    status,
)
from fastapi.responses import Response

# ? Router Configuration
router = APIRouter(
    prefix="/api/messages",
    tags=["Messages CRUD"],
    dependencies=[Security(Auth.basic)],
)


@router.options(
    path="/", operation_id="api.messages.options", responses=MessagesResponses.options
)
async def messages_options(service=Depends(MessagesService)) -> MessagesSchema:
    """Endpoint is used to find options for the `Messages` router"""
    result = service.options()
    return Response(headers={"allow": str(result)})


# ? CRUD Endpoints
@router.post(
    path="/",
    operation_id="api.messages.create",
    responses=MessagesResponses.create,
)
async def create_message(
    messages: MessagesSchema,
    background: BackgroundTasks,
    service=Depends(MessagesService),
) -> MessagesSchema:
    """Endpoint is used to create a `Messages` entity"""
    result = service.create(messages)

    return result


@router.get(
    path="/deleted",
    operation_id="api.messages.deleted",
    responses=MessagesResponses.listed,
)
async def retrieve_deleted_messages(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(MessagesService),
) -> MessagesList:
    """Endpoint is used to retrieve a list of `Messages` entities"""
    result = service.deleted(limit=limit, page_nr=page_nr)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.messages.retrieve",
    responses=MessagesResponses.retrieve,
)
async def retrieve_message(
    uuid: UUID = Path(
        description="Unique Identifier for the Messages Entity to retrieve"
    ),
    service=Depends(MessagesService),
) -> MessagesSchema:
    """Endpoint is used to retrieve a `Messages` entity"""
    result = service.retrieve(uuid)

    return result


@router.get(
    path="/", operation_id="api.messages.listed", responses=MessagesResponses.listed
)
async def retrieve_messages_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(MessagesService),
) -> MessagesList:
    """Endpoint is used to retrieve a list of `Messages` entities"""
    result = service.listed(limit=limit, page_nr=page_nr)

    return result


@router.put(
    path="/{uuid}",
    operation_id="api.messages.replace",
    responses=MessagesResponses.replace,
)
async def replace_message(
    messages: MessagesSchema,
    uuid: str = Path(
        ..., description="Unique Identifier for the Messages Entity to update"
    ),
    service=Depends(MessagesService),
) -> MessagesSchema:
    """Endpoint is used to replace a `Messages` entity"""
    result = service.replace(uuid, messages)

    return result


@router.patch(
    path="/{uuid}",
    operation_id="api.messages.update",
    responses=MessagesResponses.update,
)
async def update_message(
    messages: dict = Body(..., description="Key,value pairs to be updated"),
    uuid: str = Path(
        ..., description="Unique Identifier for the Messages Entity to update"
    ),
    service=Depends(MessagesService),
) -> MessagesSchema:
    """Endpoint is used to update a `Messages` entity"""
    result = service.update(uuid, messages)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.messages.delete",
    responses=MessagesResponses.delete,
)
async def delete_message(
    uuid: str = Path(
        ..., description="Unique Identifier for the Messages Entity to delete"
    ),
    service=Depends(MessagesService),
) -> Response:
    """Endpoint is used to delete a `Messages` entity"""
    service.delete(uuid)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
