"""File contains reuseable test fixtures"""

import base64

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """Provides an ASGI TestClient"""
    from src.acme.main import app

    # ? Arrange ...
    yield TestClient(app)


@pytest.fixture
def headers() -> dict:
    """Provides headers with default creds"""
    credentials = base64.urlsafe_b64encode("admin:admin".encode())
    return {"Authorization": f"Basic {credentials.decode()}"}
