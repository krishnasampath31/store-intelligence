from fastapi import FastAPI

app = FastAPI(
title="Store Intelligence API",
version="1.0.0"
)

@app.get("/")
def root():
return {
"service": "Store Intelligence API",
"status": "running"
}

@app.get("/health")
def health():
return {
"status": "healthy",
"stores_active": 2
}

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
"store_id": store_id,
"entry": 120,
"zone_visit": 80,
"billing": 40,
"purchase": 28
}

@app.get("/stores/{store_id}/heatmap")
def heatmap(store_id: str):
return {
"store_id": store_id,
"zones": [
{"zone": "Faces", "score": 90},
{"zone": "Loreal", "score": 75},
{"zone": "Purplle", "score": 60}
]
}

@app.get("/stores/{store_id}/anomalies")
def anomalies(store_id: str):
return {
"store_id": store_id,
"anomalies": [
{
"type": "QUEUE_SPIKE",
"severity": "WARN"
}
]
}

