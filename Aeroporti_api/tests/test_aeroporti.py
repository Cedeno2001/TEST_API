from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_aeroporti_default_pagination():
    response = client.get("/aeroporti")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_aeroporti_with_pagination():
    response = client.get("/aeroporti?page=1&size=1")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_aeroporto_by_id_success():
    response = client.get("/aeroporti/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_aeroporto_not_found():
    response = client.get("/aeroporti/999")
    assert response.status_code == 404


def test_create_aeroporto():
    payload = {
        "codice": "MXP",
        "citta": "Milano"    
    }

    response = client.post("/aeroporti", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["codice"] == payload["codice"]
    assert "id" in data
