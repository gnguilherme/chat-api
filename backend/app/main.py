"""Main module for the FastAPI application."""

from typing import Dict

from app.api import chat
from fastapi import FastAPI

app = FastAPI()

app.include_router(chat.router)


@app.get("/")
def read_root() -> Dict[str, str]:
    """Root endpoint for the FastAPI application.

    Returns
    -------
        Dict[str, str]: A welcome message.

    """
    return {"message": "Welcome to the Chat API!"}
