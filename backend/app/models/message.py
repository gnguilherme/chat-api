"""Data models for message objects."""

from pydantic import BaseModel


class Message(BaseModel):
    """Use this data model to parse the request body JSON."""

    user_message: str
    response: str
