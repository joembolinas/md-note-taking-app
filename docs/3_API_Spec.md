# API Specification (Draft)

## 1. Notes

### Save Note
- **Endpoint:** `POST /notes/`
- **Description:** Save a new markdown note.
- **Request Body:** JSON
    ```json
    {
      "filename": "my_note.md",
      "content": "# Hello World"
    }
    ```
- **Response:** `201 Created`
    ```json
    {
      "filename": "my_note.md",
      "status": "saved"
    }
    ```

### List Notes
- **Endpoint:** `GET /notes/`
- **Description:** Get a list of all saved files.
- **Response:** `200 OK`
    ```json
    {
      "files": ["my_note.md", "todo.md"]
    }
    ```

### Render Note
- **Endpoint:** `POST /notes/render`
- **Description:** Render raw markdown to HTML.
- **Request Body:** JSON
    ```json
    {
      "content": "# Title\nBold text"
    }
    ```
- **Response:** `200 OK`
    ```json
    {
      "html": "<h1>Title</h1><p><strong>Bold text</strong></p>"
    }
    ```

## 2. Grammar

### Check Grammar
- **Endpoint:** `POST /grammar/check`
- **Description:** Check the grammar of the provided text.
- **Request Body:** JSON
    ```json
    {
      "text": "This are wrong."
    }
    ```
- **Response:** `200 OK`
    ```json
    {
      "matches": [
        {
          "message": "Did you mean 'This is'?",
          "offset": 0,
          "length": 4,
          "replacements": ["This is"]
        }
      ]
    }
    ```
