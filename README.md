# JobPulse
   Real-time job market intelligence system that streams job data, processes it using Kafka-based pipelines, and visualizes insights through an interactive dashboard.

## Features

   * Real-time data ingestion
   * Kafka-based streaming pipeline
   * ETL processing and skill extraction
   * Dual database storage (PostgreSQL + MongoDB)
   * Live dashboard visualization
   * Anomaly detection on job trends

## Tech Stack

   * Python
   * Apache Kafka
   * PostgreSQL
   * MongoDB
   * Streamlit
   * Airflow (planned)

## 🔹 Functional Requirements
    Your system MUST:
    - Ingest job data (real-time or near real-time)
    - Stream data through Apache Kafka
    - Process + clean data (ETL)
    - Extract skills
    - Store data:
        - PostgreSQL
        - MongoDB
    - Show dashboard via Streamlit
    - Detect anomalies (ML)

## 🔹 Non-Functional Requirements (THIS IS WHAT MOST PEOPLE MISS)
    Scalability (Kafka handles load)
    Fault tolerance (retry logic)
    Data consistency
    Low latency
    Logging + monitoring

## High-Level Architecture
    Scraper/API
       ↓
    Python Producer
       ↓
    Kafka (jobs_topic)
       ↓
    Consumer (ETL + Skill Extraction)
       ↓
    PostgreSQL + MongoDB
       ↓
    Streamlit Dashboard
       ↓
    ML (Anomaly Detection)
 
## initial Folder Structure
      jobpulse/
      │
      ├── api/
         ├── main.py
         ├── db.py
         ├── models.py
      ├── producer/
         │
         ├── producer.py
         ├── scraper.py
         ├── utils.py
         └── config.py
      ├── consumer/
         │
         ├── consumer.py
         ├── db_postgres.py
         ├── db_mongo.py
         ├── etl.py
         └── config.py
      ├── etl/
      ├── db/
      ├── dashboard/
      ├── ml/
      ├── config/
      ├── tests/
      ├── docs/
      │
      ├── docker-compose.yml
      ├── requirements.txt
      ├── README.md
      └── .env.example

## Setup

(coming soon)