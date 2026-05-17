from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from app.database.database import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    report_id = Column(Integer)

    user1_id = Column(Integer)

    user2_id = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)