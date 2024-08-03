"""This module contains the service for the OpenAI API."""

from openai import AzureOpenAI

llm = AzureOpenAI()


async def get_response(user_message: str) -> str:
    """Return a response from the chatbot.

    Args:
    ----
        user_message (str): The user's message.

    Returns:
    -------
        str: The chatbot's response.

    """
    response = llm.chat.completions.create(
        model="gpt4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message["content"]
