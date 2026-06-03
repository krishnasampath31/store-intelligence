from fastapi import FastAPI
from app.models import Event

app = FastAPI(
title="Store Intelligence API",
version="1.0.0"
)

events_db = []

@app.get("/")
def root():
return {
"service": "Store Intelligence API",
"status": "running"
}

@app.post("/events/ingest")
def ingest(events: list[Event]):
inserted = 0

```
for event in events:
    events_db.append(event.dict())
    inserted += 1

return {
    "status": "success",
    "inserted": inserted
}
```

@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):
return {
"store_id": store_id,
"unique_visitors": 120,
"conversion_rate": 0.24,
"avg_dwell_time": 95,
"queue_depth": 3
}

@app.get("/stores/{store_id}/funnel")
def funnel(store_id: str):
return {
"entry": 120,
"zone_visit": 80,
"billing": 40,
"purchase": 28
}

@app.get("/stores/{store_id}/heatmap")
def heatmap(store_id: str):
return {
"zones": [
{"zone": "Faces", "score": 90},
{"zone": "Purplle", "score": 70}
]
}

@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str):
return {
"anomalies": [
{
"type": "QUEUE_SPIKE",
"severity": "WARN",
"suggested_action": "Open another billing counter"
}
]
}

@app.get("/health")
def health():
return {
"status": "healthy",
"last_event_count": len(events_db)
}
