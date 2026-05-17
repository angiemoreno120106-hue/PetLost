from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base


class Report(Base):

    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=False)

    pet_type = Column(String, nullable=False)

    pet_color = Column(String)

    status = Column(String, nullable=False)

    location = Column(String, nullable=False)

    image_url = Column(String)

    user_id = Column(Integer, nullable=False)

    date_reported = Column(DateTime, default=datetime.utcnow)
