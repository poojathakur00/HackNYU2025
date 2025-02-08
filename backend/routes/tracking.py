from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


# Data model for tracking screen time
class ScreenTimeEntry(BaseModel):
    user_id: str
    app_name: str  # e.g., "YouTube", "Netflix"
    duration: int  # In seconds
    timestamp: datetime


# In-memory storage (Replace with DB later)
screen_time_data = []


@router.post("/track")
async def track_screen_time(entry: ScreenTimeEntry):
    screen_time_data.append(entry.dict())
    return {"message": "Screen time logged successfully!", "entry": entry}

@router.get("/summary/{user_id}")
async def get_screen_time_summary(user_id: str):
    user_data = [entry for entry in screen_time_data if entry["user_id"] == user_id]
    return {"user_id": user_id, "total_entries": len(user_data), "data": user_data}

