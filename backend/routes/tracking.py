from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from database import SessionLocal, ScreenTimeEntry

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic model for request validation
class ScreenTimeRequest(BaseModel):
    user_id: str
    app_name: str
    duration: int  # in seconds
    timestamp: datetime

# API Route to Log Screen Time (POST request)
@router.post("/track")
async def track_screen_time(entry: ScreenTimeRequest, db: Session = Depends(get_db)):
    db_entry = ScreenTimeEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    return {"message": "Screen time logged successfully!", "entry": entry}

# API Route to Fetch User's Screen Time Summary (GET request)
@router.get("/summary/{user_id}")
async def get_screen_time_summary(user_id: str, db: Session = Depends(get_db)):
    user_data = db.query(ScreenTimeEntry).filter(ScreenTimeEntry.user_id == user_id).all()
    total_time = sum(entry.duration for entry in user_data)
    return {"user_id": user_id, "total_time": total_time, "entries": user_data}
