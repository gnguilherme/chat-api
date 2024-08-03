"""This module contains the service for the OpenAI API."""

from app.models.message import Message
from openai import AzureOpenAI

llm = AzureOpenAI()


async def get_response(user_message: str) -> Message:
    """Return a response from the chatbot.

    Args:
    ----
        user_message (str): The user's message.

    Returns:
    -------
        Message: The chatbot's response.

    """
    response = llm.chat.completions.create(
        model="gpt4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    return Message(user_message=user_message, response=response.choices[0].message.content)
