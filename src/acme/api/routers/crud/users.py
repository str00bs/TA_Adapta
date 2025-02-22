"""File contains router for '/users' CRUD endpoints"""

from uuid import UUID

from api.auth import Auth
from api.responses import UsersResponses
from api.schema import UsersList, UsersSchema
from api.services import UsersService
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
    prefix="/api/users",
    tags=["Users CRUD"],
    dependencies=[Security(Auth.basic)],
)


@router.options(
    path="/", operation_id="api.users.options", responses=UsersResponses.options
)
async def users_options(service=Depends(UsersService)) -> UsersSchema:
    """Endpoint is used to find options for the `Users` router"""
    result = service.options()
    return Response(headers={"allow": str(result)})


# ? CRUD Endpoints
@router.post(
    path="/",
    operation_id="api.users.create",
    responses=UsersResponses.create,
)
async def create_user(
    users: UsersSchema,
    background: BackgroundTasks,
    service=Depends(UsersService),
) -> UsersSchema:
    """Endpoint is used to create a `Users` entity"""
    result = service.create(users)

    return result


@router.get(
    path="/deleted",
    operation_id="api.users.deleted",
    responses=UsersResponses.listed,
)
async def retrieve_deleted_users(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(UsersService),
) -> UsersList:
    """Endpoint is used to retrieve a list of `Users` entities"""
    result = service.deleted(limit=limit, page_nr=page_nr)

    return result


@router.get(
    path="/{uuid}",
    operation_id="api.users.retrieve",
    responses=UsersResponses.retrieve,
)
async def retrieve_user(
    uuid: UUID = Path(description="Unique Identifier for the Users Entity to retrieve"),
    service=Depends(UsersService),
) -> UsersSchema:
    """Endpoint is used to retrieve a `Users` entity"""
    result = service.retrieve(uuid)

    return result


@router.get(
    path="/",
    operation_id="api.users.listed",
    responses=UsersResponses.listed,
)
async def retrieve_users_list(
    page_nr: int = Query(1, description="Page number to retrieve", ge=1),
    limit: int = Query(10, description="Number of items to retrieve", ge=1),
    service=Depends(UsersService),
) -> UsersList:
    """Endpoint is used to retrieve a list of `Users` entities"""
    result = service.listed(limit=limit, page_nr=page_nr)

    return result


@router.put(
    path="/{uuid}",
    operation_id="api.users.replace",
    responses=UsersResponses.replace,
)
async def replace_user(
    users: UsersSchema,
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to update"
    ),
    service=Depends(UsersService),
) -> UsersSchema:
    """Endpoint is used to replace a `Users` entity"""
    result = service.replace(uuid, users)

    return result


@router.patch(
    path="/{uuid}",
    operation_id="api.users.update",
    responses=UsersResponses.update,
)
async def update_user(
    users: dict = Body(..., description="Key,value pairs to be updated"),
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to update"
    ),
    service=Depends(UsersService),
) -> UsersSchema:
    """Endpoint is used to update a `Users` entity"""
    result = service.update(uuid, users)

    return result


@router.delete(
    path="/{uuid}",
    operation_id="api.users.delete",
    responses=UsersResponses.delete,
)
async def delete_user(
    uuid: str = Path(
        ..., description="Unique Identifier for the Users Entity to delete"
    ),
    service=Depends(UsersService),
) -> Response:
    """Endpoint is used to delete a `Users` entity"""
    service.delete(uuid)

    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
