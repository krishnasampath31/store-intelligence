# Store Intelligence System

Purplle Tech Challenge 2026 Submission

## Overview

This project builds an end-to-end Store Intelligence System from raw CCTV footage.

Pipeline:

CCTV Footage → Detection → Tracking → Event Generation → Analytics API → Dashboard

## Features

* Entry and Exit Detection
* Visitor Tracking
* Zone Analytics
* Billing Queue Monitoring
* Conversion Funnel Analytics
* Heatmap Analytics
* Anomaly Detection
* Health Monitoring

## API Endpoints

* POST /events/ingest
* GET /stores/{id}/metrics
* GET /stores/{id}/funnel
* GET /stores/{id}/heatmap
* GET /stores/{id}/anomalies
* GET /health

## Technology Stack

* Python
* FastAPI
* OpenCV
* YOLO
* SQLite
* Docker

## Running

```bash
docker compose up
```

## Dataset

Dataset and CCTV footage are excluded from this repository as per challenge rules.
