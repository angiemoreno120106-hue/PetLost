from pydantic import BaseModel
from datetime import datetime


class ConversationCreate(BaseModel):

    report_id: int
    user1_id: int
    user2_id: int


class ConversationResponse(BaseModel):

    id: int
    report_id: int
    user1_id: int
    user2_id: int
    created_at: datetime

    class Config:
        from_attributes = True