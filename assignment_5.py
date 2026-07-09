from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

events = [
    {
        "id": 1,
        "title": "Python Backend Workshop",
        "category": "Workshop",
        "location": "Hyderabad",
        "date": "2026-07-20",
        "organizer": "Code Club",
        "capacity": 100,
        "is_open": True,
    },
    {
        "id": 2,
        "title": "Tech Career Fair",
        "category": "Career",
        "location": "Bengaluru",
        "date": "2026-07-25",
        "organizer": "Career Connect",
        "capacity": 300,
        "is_open": True,
    },
    {
        "id": 3,
        "title": "Cultural Evening",
        "category": "Cultural",
        "location": "Hyderabad",
        "date": "2026-08-02",
        "organizer": "Arts Forum",
        "capacity": 500,
        "is_open": False,
    },
]


class EventCreate(BaseModel):
    title: str
    category: str
    location: str
    date: str
    organizer: str
    capacity: int
    is_open: bool


class EventUpdate(BaseModel):
    title: str
    category: str
    location: str
    date: str
    organizer: str
    capacity: int
    is_open: bool


class EventPatch(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    organizer: Optional[str] = None
    capacity: Optional[int] = None
    is_open: Optional[bool] = None


@app.get("/")
def home():
    return {"message": "Events API is running"}


@app.get("/events/{event_id}")
def get_events(event_id: int):
    for filtered_event in events:
        if filtered_event["id"] == event_id:
            return filtered_event
    raise HTTPException(status_code=404, detail="Event not found")


@app.get("/events")
def get_single_event(
    category: Optional[str] = None,
    location: Optional[str] = None,
    is_open: Optional[bool] = None,
):
    filtered_events = []
    if category:
        for event in events:
            if event["category"].lower() == category.lower():
                filtered_events.append(event)
    if location:
        for event in filtered_events:
            if event["location"].lower() == location.lower() and event not in filtered_events:
                filtered_events.append(event)
    if is_open is not None:
        for event in filtered_events and event not in filtered_events:
            if event["is_open"] == is_open:
                filtered_events.append(event)
    if filtered_events:
        return filtered_events
    return events


@app.post("/events")
def create_event(event: EventCreate):
    new_id = max([i["id"] for i in events], default=0) + 1

    new_event = {
        "id": new_id,
        "title": event.title,
        "category": event.category,
        "location": event.location,
        "date": event.date,
        "organizer": event.organizer,
        "capacity": event.capacity,
        "is_open": event.is_open,
    }

    events.append(new_event)

    return {"message": "Event created successfully", "event": new_event}


@app.put("/events/{event_id}")
def update_event(event_id: int, updated_event: EventUpdate):
    for event in events:
        if event["id"] == event_id:
            event.update(updated_event.model_dump())
            return {"Message": "Updated Sucessfully", "Event": event}
    raise HTTPException(status_code=404, detail="Event not found")


@app.patch("/events/{event_id}")
def patch_event(event_id: int, patch_movie: EventPatch):
    for event in events:
        if event["id"] == event_id:
            event.update(patch_movie.model_dump(exclude_none=True))
            return {"Message": "Updated Sucessfully", "Event": event}
    raise HTTPException(status_code=404, detail="Event not found")


@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    for event in events:
        if event["id"] == event_id:
            events.remove(event)
            return {"message": "Event deleted successfully", "event": event}
    raise HTTPException(status_code=404, detail="Movie not Found")
