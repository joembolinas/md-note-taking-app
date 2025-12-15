# Markdown Note-Taking App

![Markdown Note-taking App](https://assets.roadmap.sh/guest/markdown-note-taking-app-tymi3.png)

A robust, systematic backend implementation for the [Markdown Note-taking App](https://roadmap.sh/projects/markdown-note-taking-app) challenge from roadmap.sh. Built with **Python** and **FastAPI**.

## Features

- **Grammar Check**: corrections for spelling and basic grammar using `TextBlob`.
- **Markdown Rendering**: Secure conversion of Markdown text to HTML.
- **File Management**: Upload, save, and retrieve note files.
- **Systematic Design**: Layered architecture with a focus on maintainability.

> [!TIP]
> This project follows a "Documentation First" engineering process. Detailed design artifacts are available in the `docs/` directory:
> *   [Roadmap](docs/0_Roadmap.md)
> *   [Product Requirements (PRD)](docs/1_PRD.md)
> *   [Architecture](docs/2_Architecture.md)

## Getting Started

### Prerequisites

- **Python 3.10+**
- **pip**

### Installation

1.  **Environment Setup**

    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Linux/macOS
    source .venv/bin/activate
    ```

2.  **Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Download NLTK Data**

    Required for the grammar checking service.

    ```bash
    python -c "import nltk; nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger_eng')"
    ```

### Running Local

Start the API server with hot-reload enabled:

```bash
uvicorn app.main:app --reload
```

The application will be served at `http://localhost:8000`.
Visit the **[Interactive API Documentation](http://localhost:8000/docs)** to explore and test the endpoints.

## Testing

Run the automated test suite to verify all endpoints:

```bash
pytest
```

## Resources

- [Roadmap.sh Project Page](https://roadmap.sh/projects/markdown-note-taking-app)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
