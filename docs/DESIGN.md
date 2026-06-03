# DESIGN.md

# Store Intelligence System Architecture

## Overview

The goal of this system is to convert raw CCTV footage into actionable retail analytics. The system processes entry cameras, floor cameras, and billing cameras to generate structured behavioural events and expose store intelligence through APIs.

## Architecture

Raw CCTV Videos
↓
Detection Layer (YOLO)
↓
Tracking Layer (ByteTrack)
↓
Event Generation
↓
Event Storage (SQLite)
↓
Analytics Engine
↓
FastAPI Endpoints
↓
Dashboard / Consumer

## Detection Layer

The detection layer uses YOLO for person detection. Every detected person is assigned a tracking identifier. Entry and exit events are generated when a tracked person crosses the virtual entrance line.

## Tracking Layer

ByteTrack is used to maintain consistent tracking IDs across frames. This allows the system to estimate dwell time, zone visits, and queue behaviour.

## Event Pipeline

The detection pipeline emits structured events such as:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_EXIT
* ZONE_DWELL
* BILLING_QUEUE_JOIN

These events are stored and later consumed by analytics modules.

## Analytics Layer

The analytics engine computes:

* Unique visitors
* Conversion rate
* Average dwell time
* Queue depth
* Funnel progression
* Heatmap statistics
* Operational anomalies

## AI-Assisted Decisions

1. AI tools were used to compare multiple detection approaches including YOLOv8, RT-DETR, and MediaPipe. YOLO was selected because of its balance between speed and accuracy.

2. AI-assisted brainstorming helped design the event schema and identify which events were required to support funnel and heatmap analytics.

3. AI suggestions were reviewed critically. Complex multi-camera re-identification was intentionally excluded from the MVP due to limited development time and increased implementation risk.

## Scalability

For larger deployments, SQLite can be replaced with PostgreSQL and event ingestion can be connected to Kafka for real-time streaming across multiple stores.

