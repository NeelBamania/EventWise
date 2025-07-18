from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Event(BaseModel):
    id: int
    title: str
    description: str

fake_event_db = []

@app.post("/api/events/")
def create_event(event: Event):
    fake_event_db.append(event.dict())
    return {"message": "Event created successfully", "event": event}

@app.get("/api/events/", response_model=List[Event])
def list_events():
    return fake_event_db
