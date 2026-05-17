from sqlalchemy.orm import Session
from app.models.conversation import Conversation
from app.models.message import Message
from app.schemas.conversation import ConversationCreate
from app.schemas.message import MessageCreate


def create_conversation(db: Session, conversation: ConversationCreate):

    new_conversation = Conversation(
        report_id=conversation.report_id,
        user1_id=conversation.user1_id,
        user2_id=conversation.user2_id
    )

    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    return new_conversation


def get_user_conversations(db: Session, user_id: int):

    return db.query(Conversation).filter(
        (Conversation.user1_id == user_id) |
        (Conversation.user2_id == user_id)
    ).all()


def create_message(db: Session, message: MessageCreate):

    new_message = Message(
        conversation_id=message.conversation_id,
        sender_id=message.sender_id,
        message=message.message
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message


def get_messages(db: Session, conversation_id: int):

    return db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).all()