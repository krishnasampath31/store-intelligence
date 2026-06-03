# PROMPT:

# Generate FastAPI API tests for health and metrics endpoints.

# CHANGES MADE:

# Simplified tests for challenge MVP.

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
response = client.get("/health")
assert response.status_code == 200

def test_metrics():
response = client.get("/stores/STORE_BLR_002/metrics")
assert response.status_code == 200

