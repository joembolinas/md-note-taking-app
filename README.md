# Markdown Note-Taking App API

A systematic, real-world backend for managing, rendering, and checking grammar of Markdown notes. Built with Python and FastAPI.

## 📚 Documentation
This project follows a rigorous engineering process. Please refer to the `docs/` folder for detailed documentation:
- **[Roadmap](docs/0_Roadmap.md):** Project phases and status.
- **[Product Requirements (PRD)](docs/1_PRD.md):** Functional specifications.
- **[Architecture](docs/2_Architecture.md):** System design and component diagrams.
- **[API Specification](docs/3_API_Spec.md):** Endpoint details.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Virtualenv (recommended)

### Installation
1.  **Clone the repository** (if not already done).
2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Linux/Mac
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Download Grammar Data:**
    ```bash
    python -c "import nltk; nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger_eng')"
    ```

### Running the App
Start the server using Uvicorn:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.
Access the interactive API docs at `http://localhost:8000/docs`.

### Running Tests
Execute the test suite using Pytest:
```bash
pytest tests
```

## 🛠 Features
- **Save Notes:** Upload and store markdown files securely.
- **Render HTML:** Convert markdown text to clean HTML.
- **Grammar Check:** Basic grammar/spelling analysis using TextBlob.
- **Systematic Design:** Layered architecture (API -> Services -> Storage).

---

## 🔗 Project Attribution
This project is an implementation of the [Markdown Note-taking App](https://roadmap.sh/projects/markdown-note-taking-app) project from roadmap.sh.
