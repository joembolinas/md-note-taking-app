# Product Requirements Document (PRD)

## 1. Introduction
The Markdown Note-Taking App is a backend service designed to manage, render, and grammar-check markdown notes. It allows users to upload/save raw markdown text, retrieve rendered HTML, and perform grammar analysis.

## 2. Goals
- Provide a robust API for markdown management.
- Demonstrate parsing and rendering capabilities.
- Integrate external logic (grammar checking) into a RESTful flow.

## 3. User Stories
- **US-1:** As a user, I want to save a markdown note so that I can access it later.
- **US-2:** As a user, I want to list all my saved notes to see what I have written.
- **US-3:** As a user, I want to view the HTML representation of a note to see how it looks formatted.
- **US-4:** As a user, I want to check the grammar of a note to ensure it is correct.

## 4. Functional Requirements

### 4.1 Note Management
- **FR-1 (Save):** The system MUST provide an endpoint to accept Markdown text and save it as a file.
    - *Input:* JSON with filename and content, or Multipart file upload.
    - *Storage:* Local filesystem (for MVP).
- **FR-2 (List):** The system MUST provide an endpoint to list all saved markdown files.

### 4.2 Processing
- **FR-3 (Render):** The system MUST provide an endpoint that accepts markdown text (or a file ID) and returns the rendered HTML.
- **FR-4 (Grammar):** The system MUST provide an endpoint to check the grammar of the provided text.
    - *Implementation:* Use a Python library (e.g., `language-tool-python`) or a placeholder API if strictly local.

## 5. Non-Functional Requirements
- **Performance:** Rendering should happen in under 200ms for typical note sizes (<10KB).
- **Tech Stack:** Python (Framework TBD in Architecture).
- **Usability:** API error messages should be clear and descriptive.

## 6. Out of Scope (MVP)
- User Authentication/Authorization.
- Database storage (Filesystem is sufficient).
- Frontend UI (This is a backend-focused project).
