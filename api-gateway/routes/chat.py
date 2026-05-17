from fastapi import APIRouter
import requests

router = APIRouter(prefix="/chat", tags=["Chat"])

CHAT_SERVICE = "http://localhost:8003"


@router.post("/conversations")
def create_conversation(data: dict):
    response = requests.post(
        f"{CHAT_SERVICE}/chat/conversations",
        json=data
    )
    return response.json()


@router.get("/conversations/{user_id}")
def get_conversations(user_id: int):
    response = requests.get(
        f"{CHAT_SERVICE}/chat/conversations/{user_id}"
    )
    return response.json()


@router.post("/messages")
def send_message(data: dict):
    response = requests.post(
        f"{CHAT_SERVICE}/chat/messages",
        json=data
    )
    return response.json()


@router.get("/messages/{conversation_id}")
def get_messages(conversation_id: int):
    response = requests.get(
        f"{CHAT_SERVICE}/chat/messages/{conversation_id}"
    )
    return response.json()