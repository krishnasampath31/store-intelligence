# CHOICES.md

# Decision 1: Detection Model

## Options Considered

* YOLOv8
* RT-DETR
* MediaPipe

## AI Suggestion

AI tools suggested YOLOv8 and RT-DETR as strong candidates for retail CCTV scenarios.

## Final Choice

YOLO was selected because it offers strong real-time performance, mature tooling, and easy integration with OpenCV pipelines.

## Reasoning

The challenge prioritises a working end-to-end system. YOLO provides a practical balance between implementation speed and detection accuracy.

# Decision 2: Event Schema Design

## Options Considered

* Minimal event schema
* Rich behavioural event schema

## AI Suggestion

AI suggested using richer behavioural events to support downstream analytics.

## Final Choice

A structured event schema including visitor ID, timestamps, confidence scores, zone information, and metadata was chosen.

## Reasoning

This design supports funnel analytics, anomaly detection, and future extensibility.

# Decision 3: API Architecture

## Options Considered

* Flask
* FastAPI

## AI Suggestion

AI recommended FastAPI because of automatic validation and API documentation support.

## Final Choice

FastAPI was selected.

## Reasoning

FastAPI enables rapid development, clean request validation, and aligns well with the challenge requirements.

# Trade-Offs

Several advanced features such as Kafka streaming, distributed event processing, and multi-camera re-identification were considered but intentionally excluded from the MVP. The focus was placed on delivering a reliable analytics pipeline that satisfies the required endpoints and business metrics.

