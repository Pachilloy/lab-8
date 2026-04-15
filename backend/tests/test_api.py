import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))
TEST_DB_PATH = ROOT_DIR / "test_lab8.db"
if TEST_DB_PATH.exists():
    TEST_DB_PATH.unlink()
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH.resolve()}"

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) >= 3


def test_create_book():
    payload = {"title": "Vue Handbook", "author": "Frontend Team", "genre": "Web", "price": 28.5, "year": 2024}
    response = client.post("/books", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
