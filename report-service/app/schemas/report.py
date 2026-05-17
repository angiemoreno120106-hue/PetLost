from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class PetType(str, Enum):
    perro = "perro"
    gato = "gato"
    otro = "otro"

class ReportStatus(str, Enum):
    perdida = "perdida"
    encontrada = "encontrada"
    recuperada = "recuperada"


class ReportCreate(BaseModel):

    title: str

    description: str

    pet_type: PetType

    pet_color: Optional[str]

    status: ReportStatus

    location: str

    image_url: Optional[str]

    user_id: int


class ReportResponse(BaseModel):

    id: int

    title: str

    description: str

    pet_type: PetType

    pet_color: Optional[str]

    status: ReportStatus

    location: str

    image_url: Optional[str]

    user_id: int

    date_reported: datetime

    class Config:
        from_attributes = True