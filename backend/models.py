from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from database import Base


class Conversation(Base):
    """Represents one customer support conversation turn."""

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), nullable=False, index=True)
    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    status = Column(String(50), nullable=False, default="AI_MODE")
    language = Column(String(10), nullable=False, default="uz")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
