import markdown
from app.core import storage

def save_note(filename: str, content: str) -> str:
    return storage.save_file(filename, content)

def list_notes() -> list[str]:
    return storage.list_files()

def render_text(content: str) -> str:
    """
    Convert markdown text to HTML.
    """
    return markdown.markdown(content)

def get_rendered_note(filename: str) -> str:
    """
    Retrieve a note and render it to HTML.
    """
    content = storage.read_file(filename)
    return render_text(content)
