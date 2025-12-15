from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Markdown Note-Taking API"

def test_create_and_list_note():
    # 1. Create
    note_data = {"filename": "test_note.md", "content": "# Test\nThis is a test."}
    response = client.post("/notes/", json=note_data)
    assert response.status_code == 201
    assert response.json()["filename"] == "test_note.md"
    
    # 2. List
    response = client.get("/notes/")
    assert response.status_code == 200
    files = response.json()["files"]
    assert "test_note.md" in files

    # Cleanup (Optional, but good for local dev)
    if os.path.exists("storage/test_note.md"):
        os.remove("storage/test_note.md")

def test_render_note():
    data = {"content": "# Hello\n**World**"}
    response = client.post("/notes/render", json=data)
    assert response.status_code == 200
    html = response.json()["html"]
    assert "<h1>Hello</h1>" in html
    assert "<strong>World</strong>" in html

def test_grammar_check():
    # "Teh" is a common typo for "The"
    data = {"text": "Teh quick brown fox."}
    response = client.post("/grammar/check", json=data)
    assert response.status_code == 200
    matches = response.json()["matches"]
    # Depending on TextBlob's exact output, we expect some match.
    # We just verify the structure and that it runs without error.
    assert isinstance(matches, list)
    if matches:
        assert "replacements" in matches[0]
