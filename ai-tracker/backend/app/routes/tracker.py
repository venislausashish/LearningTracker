from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas import DayUpdate
from ..services import tracker_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/days")
def get_days(db: Session = Depends(get_db)):
    return tracker_service.get_all_days(db)

@router.put("/days/{day_id}")
def update_day(day_id: int, data: DayUpdate, db: Session = Depends(get_db)):
    updated = tracker_service.update_day(
        db, day_id, data.completed, data.notes
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Day not found")
    return updated