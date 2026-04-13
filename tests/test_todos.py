import sys
from pathlib import Path

# добавить корень проекта в sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_read_todo():
    # 1. Neues Todo erstellen
    payload = {
        "title": "Test Todo",
        "description": "Beschreibung",
        "status": "todo",
        "due_date": None,
    }
    create_response = client.post("/todos", json=payload)
    assert create_response.status_code == 200
    data = create_response.json()
    assert data["title"] == payload["title"]
    todo_id = data["id"]

    # 2. Lese das erstellte Todo
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 200
    data_get = get_response.json()
    assert data_get["id"] == todo_id
    assert data_get["title"] == payload["title"]