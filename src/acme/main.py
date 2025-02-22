"""
Main Application file
- Used as target when running the ASGI server; `uvicorn main:app --reload`
- Collects routers and mounts/includes them to the API
"""

from pathlib import Path

import psycopg2.extras
from api.routers import routers
from config import Config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# ? Required so postgres understands <UUID>
psycopg2.extras.register_uuid()

# ? Initialize application with configs
app = FastAPI(**Config.API.model_dump())

# ? Mount & serve the frontend
app.mount(
    path="/frontend",
    app=StaticFiles(directory=Path(__file__).parent.joinpath("frontend")),
    name="frontend",
)

# ? Add the routers
for router in routers:
    app.include_router(router)
