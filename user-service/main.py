from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes.user_routes import router

app = FastAPI(title="User Service - PetLost")

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "User Service funcionando 🚀"}


@app.post("/register")
def register(user: dict):
    return {"message": "Usuario registrado"}

@app.post("/login")
def login(user: dict):
    return {"message": "Login correcto"}