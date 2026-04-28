from pydantic import BaseModel

class DayUpdate(BaseModel):
    completed: bool
    notes: str | None = None