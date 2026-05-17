from fastapi import FastAPI

from app.database.database import Base, engine
from app.routes.chat_routes import router as chat_router

from app.models import conversation
from app.models import message


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PetLost Chat Service"
)

app.include_router(chat_router)