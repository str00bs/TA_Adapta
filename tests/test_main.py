"""File contains tests for the main file and pages"""


def test_docs(client):
    # ? Act
    response = client.get("/docs")

    # ? Assert
    assert response.status_code == 200
    assert "<!DOCTYPE html" in response.text
    assert "swagger" in response.text


def test_redoc(client):
    # ? Act
    response = client.get("/redoc")

    # ? Assert
    assert response.status_code == 200
    assert "<!DOCTYPE html" in response.text
    assert "redoc" in response.text


def test_openapi(client):
    # ? Act
    response = client.get("/openapi.json")
    data = response.json()

    # ? Assert
    assert response.status_code == 200
    assert "openapi" in data.keys()
