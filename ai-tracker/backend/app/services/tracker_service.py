from sqlalchemy.orm import Session
from ..models import Day

def get_all_days(db: Session):
    return db.query(Day).all()

def update_day(db: Session, day_id: int, completed: bool, notes: str | None):
    day = db.query(Day).filter(Day.id == day_id).first()
    if not day:
        return None

    day.completed = completed
    if notes is not None:
        day.notes = notes

    db.commit()
    db.refresh(day)
    return day