# Pydantic schemas
from typing import Optional

from pydantic import BaseModel
from datetime import datetime

# --- Request from client ---
class ChatRequest(BaseModel):
    username: str
    message: str

# --- Response to client ---
class ChatResponse(BaseModel):
    response: str

# --- DB Object Response (optional, for admin/dashboard) ---
class MessageSchema(BaseModel):
    id: int
    convo_id: int
    sender: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

class ConversationSchema(BaseModel):
    id: int
    user_id: int
    title: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
