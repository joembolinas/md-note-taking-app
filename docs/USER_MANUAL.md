# User Manual: Markdown Note-Taking App

## 1. Introduction
Welcome to the **Markdown Note-Taking App**. This application provides a robust API for creating, managing, and rendering Markdown notes, complete with basic grammar checking capabilities.

It is designed to be run locally and interacted with via HTTP requests or the built-in interactive Swagger UI.

---

## 2. Getting Started

### Prerequisites
- **Python 3.10+** installed on your system.

### Installation
1.  Navigate to the project root directory in your terminal.
2.  Create a virtual environment (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If you encounter issues with `textblob` corpora, the app attempts to download them automatically. If that fails, see Troubleshooting.*

### Running the Application
Start the server using the following command:
```bash
python -m app.main
```
You should see output indicating the server is running, typically at `http://0.0.0.0:8000`.

---

## 3. Using the Feature Features

The easiest way to explore and use the features is via the **Interactive API Documentation**.

1.  Open your browser.
2.  Go to **[http://localhost:8000/docs](http://localhost:8000/docs)**.

This interface allows you to execute requests directly from your browser.

### Key Features & Usage

#### A. Create a Note
**Endpoint:** `POST /notes/`

Save a new markdown file to the storage.

-   **Input (JSON):**
    ```json
    {
      "filename": "my_first_note",
      "content": "# Hello World\nThis is a markdown note."
    }
    ```
-   **Action:** Saves `my_first_note.md` to `storage/`.

#### B. List Notes
**Endpoint:** `GET /notes/`

Retrieve a list of all saved notes.

-   **Output:** Returns a list of filenames available in storage.

#### C. Render Markdown (Preview)
**Endpoint:** `POST /notes/render`

Convert raw Markdown text into HTML without saving it. Useful for live previews.

-   **Input (JSON):**
    ```json
    {
      "content": "**Bold text** and *italics*."
    }
    ```
-   **Output:** `<b>Bold text</b> and <i>italics</i>.`

#### D. Render Saved Note
**Endpoint:** `GET /notes/{filename}/render`

View the HTML representation of a note already saved in storage.

-   **path-param:** `filename` (e.g., `my_first_note`)
-   **Output:** The HTML content of the file.

#### E. check Grammar
**Endpoint:** `POST /grammar/check`

Analyze text for spelling and basic grammar issues.

-   **Input (JSON):**
    ```json
    {
      "text": "I hav a dreem."
    }
    ```
-   **Output:** simple spelling corrections/suggestions (e.g., "I have a dream").

---

## 4. Troubleshooting

*   **`ModuleNotFoundError`**: Ensure you are running the command from the root folder (`d:\devfiles\mini-project\md-note-taking-app`) and using `python -m app.main`.
*   **Port already in use**: If port 8000 is taken, the app will fail to start. Update `app/main.py` or free up the port.
*   **NLTK Errors**: If you see errors about missing "punkt" or "averaged_perceptron_tagger", run the following python snippet manually:
    ```python
    import nltk
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')
    ```
