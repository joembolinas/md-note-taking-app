from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.schemas import (
    NoteCreate, NoteResponse, NoteList, 
    RenderRequest, RenderResponse, 
    GrammarRequest, GrammarResponse
)
from app.services import note_service, grammar_service

router = APIRouter()

# --- Notes Endpoints ---

@router.post("/notes/", response_model=NoteResponse, status_code=201)
async def create_note(note: NoteCreate):
    """
    Save a markdown note.
    """
    saved_name = note_service.save_note(note.filename, note.content)
    return NoteResponse(filename=saved_name, status="saved")

@router.get("/notes/", response_model=NoteList)
async def list_notes():
    """
    List all saved notes.
    """
    files = note_service.list_notes()
    return NoteList(files=files)

@router.post("/notes/render", response_model=RenderResponse)
async def render_note(request: RenderRequest):
    """
    Render raw markdown text to HTML.
    """
    html_content = note_service.render_text(request.content)
    return RenderResponse(html=html_content)

@router.get("/notes/{filename}/render", response_model=RenderResponse)
async def render_saved_note(filename: str):
    """
    Render a saved note to HTML.
    """
    try:
        html_content = note_service.get_rendered_note(filename)
        return RenderResponse(html=html_content)
    except Exception as e:
         raise HTTPException(status_code=404, detail="Note not found")

# --- Grammar Endpoints ---

@router.post("/grammar/check", response_model=GrammarResponse)
async def check_grammar(request: GrammarRequest):
    """
    Check the grammar (spelling) of the provided text.
    """
    matches = grammar_service.check_grammar(request.text)
    return GrammarResponse(matches=matches)
