"""File contains router for `/api/system` endpoint(s)"""

from api.responses import SystemResponses
from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates

# ? Router setup
templates = Jinja2Templates(directory="frontend/templates")
router = APIRouter(
    tags=["System"],
)


# ? Router endpoints
@router.get(
    path="/",
    operation_id="api.system.index",
    responses=SystemResponses.index,
)
async def index(request: Request) -> Response:
    """Serves frontend template"""
    return templates.TemplateResponse(request, "pages/index.html")
