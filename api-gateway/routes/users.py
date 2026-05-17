from fastapi import APIRouter
import requests

router = APIRouter(prefix="/users", tags=["Users"])

USER_SERVICE = "http://localhost:8001"


@router.get("/")
def get_users():
    response = requests.get(f"{USER_SERVICE}/users")
    return response.json()


@router.post("/")
def create_user(user: dict):
    response = requests.post(
        f"{USER_SERVICE}/users",
        json=user
    )
    return response.json()


@router.get("/{user_id}")
def get_user(user_id: int):
    response = requests.get(f"{USER_SERVICE}/users/{user_id}")
    return response.json()


@router.put("/{user_id}")
def update_user(user_id: int, user: dict):
    response = requests.put(
        f"{USER_SERVICE}/users/{user_id}",
        json=user
    )
    return response.json()


@router.delete("/{user_id}")
def delete_user(user_id: int):
    response = requests.delete(f"{USER_SERVICE}/users/{user_id}")
    return response.json()