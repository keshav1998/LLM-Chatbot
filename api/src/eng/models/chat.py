from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

class Chat(BaseModel):
    question: str
    description: str | None = None
