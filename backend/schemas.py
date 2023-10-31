from pydantic import BaseModel


class MessageCreate(BaseModel):
    sender: str
    content: str
