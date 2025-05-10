# chat.py – Chat schema
from pydantic import BaseModel

class ChatPrompt(BaseModel):
    prompt: str