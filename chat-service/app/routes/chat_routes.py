from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import SessionLocal
from app.schemas.conversation import ConversationCreate, ConversationResponse
from app.schemas.message import MessageCreate, MessageResponse
from app.services import chat_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/conversations", response_model=ConversationResponse)
def create_conversation(
        conversation: ConversationCreate,
        db: Session = Depends(get_db)
):

    return chat_service.create_conversation(db, conversation)


@router.get("/conversations/{user_id}", response_model=List[ConversationResponse])
def get_conversations(user_id: int, db: Session = Depends(get_db)):

    return chat_service.get_user_conversations(db, user_id)


@router.post("/messages", response_model=MessageResponse)
def send_message(message: MessageCreate, db: Session = Depends(get_db)):

    return chat_service.create_message(db, message)


@router.get("/messages/{conversation_id}", response_model=List[MessageResponse])
def get_messages(conversation_id: int, db: Session = Depends(get_db)):

    return chat_service.get_messages(db, conversation_id)