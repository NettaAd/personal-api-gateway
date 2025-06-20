from fastapi.testclient import TestClient
from services.book_tracker.main import app

client = TestClient(app)

def test_create_and_get_book():
    response = client.post("/books", json={"title": "1984", "author": "George Orwell"})
    assert response.status_code == 200
    book = response.json()
    assert "id" in book
    assert book["title"] == "1984"

    # Get the book
    get_response = client.get(f"/books/{book['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == book
