# System Architecture Design

## 1. Overview
The application follows a **Layered Architecture** pattern to ensure separation of concerns. It is built as a RESTful API using Python.

## 2. Technology Stack
- **Language:** Python 3.10+
- **Web Framework:** FastAPI (chosen for type safety, async support, and auto-docs).
- **Server:** Uvicorn (ASGI server).
- **Markdown Processing:** `markdown` library (standard, extensible).
- **Grammar Checking:** `language-tool-python` (wrapper for LanguageTool) or `textblob`.
- **Storage:** Local Filesystem (managing `.md` files in a `storage/` directory).

## 3. High-Level Components

```mermaid
graph TD
    Client[Client / API Consumer] --> API[API Layer (FastAPI Routers)]
    API --> Service[Service Layer]
    
    subgraph Services
    Service --> NoteService[Note Service]
    Service --> GrammarService[Grammar Service]
    end
    
    NoteService --> FS[File System Adapter]
    NoteService --> MD[Markdown Renderer]
    GrammarService --> LT[LanguageTool Engine]
    
    FS --> Disk[(Local Storage)]
```

## 4. Component Responsibilities

### 4.1 API Layer (`app/api/`)
- Handles HTTP requests and responses.
- Validates input using Pydantic models.
- Delegates business logic to Services.
- **Endpoints:**
    - `POST /notes/`: Upload/Save a note.
    - `GET /notes/`: List all notes.
    - `POST /notes/render`: Render markdown to HTML.
    - `POST /grammar/check`: Check text grammar.

### 4.2 Service Layer (`app/services/`)
- **NoteService:** Orchestrates file I/O and rendering.
- **GrammarService:** Wraps the external grammar checking library to provide a clean internal API.

### 4.3 Data Layer (`app/core/storage.py`)
- Abstracts filesystem operations.
- Ensures safe file handling (path traversal prevention).

## 5. Directory Structure
```
md-note-taking-app/
├── app/
│   ├── api/            # Route handlers
│   ├── core/           # Config, Security, Storage utils
│   ├── models/         # Pydantic schemas
│   ├── services/       # Business logic
│   └── main.py         # Entry point
├── docs/               # Documentation
├── storage/            # Saved notes
├── tests/              # Pytest tests
└── pyproject.toml      # Dependencies
```
