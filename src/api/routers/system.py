"""File contains router for `/api/system` endpoint(s)"""

from pathlib import Path

from fastapi import APIRouter, Request, Response
from fastapi.templating import Jinja2Templates

from api.responses import SystemResponses

# ? Router setup
# Path.cwd().joinpath("src/adapta").joinpath("frontend/templates")
root_dir = Path(__file__).parent.parent.parent
templates = Jinja2Templates(directory=root_dir.joinpath("frontend/templates"))
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
