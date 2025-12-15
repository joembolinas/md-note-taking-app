
import json
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def print_section(title):
    print(f"\n{'='*50}")
    print(f" TEST: {title}")
    print(f"{'='*50}")

def run_demo():
    print("Running Live API Demo...\n")

    # 1. Grammar Check
    print_section("Grammar Check (POST /grammar/check)")
    payload = {"text": "I hav a dreem to code goood."}
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = client.post("/grammar/check", json=payload)
    print("Response Status:", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=2))

    # 2. Render Markdown
    print_section("Render Markdown (POST /notes/render)")
    payload = {"content": "# Hello World\n\nThis is **bold** and *italic* details."}
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = client.post("/notes/render", json=payload)
    print("Response Status:", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=2))

    # 3. Create Note
    print_section("Create Note (POST /notes/)")
    payload = {
        "filename": "demo_note_123.md", 
        "content": "# Saved Note\nThis note was saved via the demo script."
    }
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = client.post("/notes/", json=payload)
    print("Response Status:", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=2))

    # 4. List Notes
    print_section("List Notes (GET /notes/)")
    response = client.get("/notes/")
    print("Response Status:", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=2))

    # 5. Render Saved Note
    print_section("Render Saved Note (GET /notes/{filename}/render)")
    response = client.get("/notes/demo_note_123.md/render")
    print("Response Status:", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=2))

    # Cleanup
    if os.path.exists("storage/demo_note_123.md"):
        os.remove("storage/demo_note_123.md")
        print("\n[Cleanup] Removed temporary demo file.")

if __name__ == "__main__":
    run_demo()
