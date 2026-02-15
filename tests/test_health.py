from fastapi.testclient import TestClient

from app.api.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page_renders() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Distributor AI Catalog Assistant" in response.text
    assert "Crispy Butter Biscuits 200g" in response.text
def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
