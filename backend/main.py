from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from api.api_router import api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This will need to be restricted in production to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/", response_class=FileResponse)
async def frontend():
    return FileResponse("index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router)
