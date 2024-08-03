"""This module defines the chat API endpoint."""

from typing import Any, Dict

from app.services.llm_service import get_response
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Message(BaseModel):
    """Use this data model to parse the request body JSON."""

    user_message: str


@router.post("/chat/")
async def chat(message: Message) -> Dict[str, Any]:
    """Return a response from the chatbot.

    Args:
    ----
        message (Message): JSON body of the request.

    Returns:
    -------
        Dict[str, Any]: JSON response.

    """
    response = await get_response(message.user_message)
    return {"response": response}
