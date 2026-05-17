from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes import report_routes

app = FastAPI(
    title="PetLost Report Service"
)

Base.metadata.create_all(bind=engine, checkfirst=True)

app.include_router(report_routes.router)