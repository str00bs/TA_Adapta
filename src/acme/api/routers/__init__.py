"""Module contains API Router files and endpoint controllers"""

from .crud import crud_routers
from .system import router as SystemRouter

routers: list[object] = [*crud_routers, SystemRouter]
