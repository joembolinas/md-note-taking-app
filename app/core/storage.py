import os
import glob
from fastapi import HTTPException

# Constants
STORAGE_DIR = "storage"
ALLOWED_EXTENSIONS = {".md"}

def _get_file_path(filename: str) -> str:
    """
    Securely resolve the file path, preventing directory traversal.
    """
    # Sanitize filename (basic implementation)
    filename = os.path.basename(filename)
    if not filename.endswith(".md"):
        filename += ".md"
    
    return os.path.join(STORAGE_DIR, filename)

def save_file(filename: str, content: str) -> str:
    """
    Save content to a file in the storage directory.
    """
    filepath = _get_file_path(filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return os.path.basename(filepath)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

def list_files() -> list[str]:
    """
    List all .md files in the storage directory.
    """
    # Ensure storage dir exists
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
        
    files = glob.glob(os.path.join(STORAGE_DIR, "*.md"))
    return [os.path.basename(f) for f in files]

def read_file(filename: str) -> str:
    """
    Read content of a file.
    """
    filepath = _get_file_path(filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")
        
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")
