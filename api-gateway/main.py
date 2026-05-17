from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_SERVICE = "http://localhost:8001"


@app.post("/register")
async def register(data: dict):
    response = requests.post(f"{USER_SERVICE}/register", json=data)
    return response.json()


@app.post("/login")
async def login(data: dict):
    response = requests.post(f"{USER_SERVICE}/login", json=data)
    return response.json()