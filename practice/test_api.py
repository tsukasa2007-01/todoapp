from api_hello import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_todo_crud_flow():
    response = client.post("/api/todos", json={"title": "テストタスク"})
    assert response.status_code == 201
    todo = response.json()
    assert todo["title"] == "テストタスク"
    assert todo["done"] is False
    todo_id = todo["id"]

    response = client.get("/api/todos")
    assert response.status_code == 200
    ids = [t["id"] for t in response.json()]
    assert todo_id in ids

    response = client.put(f"/api/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["done"] is True

    response = client.delete(f"/api/todos/{todo_id}")
    assert response.status_code == 200


def test_empty_title_returns_400():
    response = client.post("/api/todos", json={"title": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "タイトルは必須です"


def test_missing_todo_returns_404():
    response = client.delete("/api/todos/999999")
    assert response.status_code == 404
