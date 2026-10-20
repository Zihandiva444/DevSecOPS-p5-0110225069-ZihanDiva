from app import create_app
from app.validators import validate_title


def test_validate_title_ok():
    assert validate_title("  Belajar DevSecOps ") == (True, "Belajar DevSecOps")


def test_validate_title_empty():
    ok, _ = validate_title("   ")
    assert ok is False


def test_create_and_list_task():
    client = create_app().test_client()
    res = client.post("/tasks", json={"title": "Tugas 1"})
    assert res.status_code == 201
    assert any(t["title"] == "Tugas 1" for t in client.get("/tasks").get_json())


def test_create_task_invalid():
    client = create_app().test_client()
    assert client.post("/tasks", json={"title": ""}).status_code == 400