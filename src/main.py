"""
Main Application file
- Used as target when running the ASGI server; `uvicorn main:app --reload`
- Collects routers and mounts/includes them to the API
"""

import psycopg2.extras
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config import Config
from router import router

# ? Required so postgres understands <UUID>
psycopg2.extras.register_uuid()


# ? Initialize application with configs
app = FastAPI(**Config.API.model_dump())

# ? Mount Static files
app.mount(
    path="/frontend",
    app=StaticFiles(directory="frontend"),
    name="frontend",
)

# ? Add the router
app.include_router(router)
