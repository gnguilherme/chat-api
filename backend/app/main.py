"""Main module for the FastAPI application."""

from typing import Dict

from app.api import chat
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(chat.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> Dict[str, str]:
    """Root endpoint for the FastAPI application.

    Returns
    -------
        Dict[str, str]: A welcome message.

    """
    return {"message": "Welcome to the Chat API!"}
