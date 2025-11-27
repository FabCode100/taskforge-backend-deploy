from fastapi import FastAPI
from .routers import agents, auth

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TaskForge-AI — MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(agents.router)
