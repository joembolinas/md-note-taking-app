from pydantic import BaseModel
from typing import List, Optional

# Note Models
class NoteCreate(BaseModel):
    filename: str
    content: str

class NoteResponse(BaseModel):
    filename: str
    status: str

class NoteList(BaseModel):
    files: List[str]

class RenderRequest(BaseModel):
    content: str

class RenderResponse(BaseModel):
    html: str

# Grammar Models
class GrammarRequest(BaseModel):
    text: str

class GrammarMatch(BaseModel):
    message: str
    offset: int
    length: int
    replacements: List[str]

class GrammarResponse(BaseModel):
    matches: List[GrammarMatch]
