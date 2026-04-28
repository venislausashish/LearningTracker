from sqlalchemy import Column, Integer, Boolean, String
from .database import Base

class Day(Base):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer, unique=True)
    task = Column(String)
    phase = Column(String)
    completed = Column(Boolean, default=False)
    notes = Column(String, default="")