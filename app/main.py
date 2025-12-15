from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Markdown Note-Taking API",
    description="A systematic API for managing and rendering markdown notes.",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Markdown Note-Taking API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

