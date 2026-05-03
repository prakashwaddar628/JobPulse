from kafka import KafkaProducer
import json
import time
from scraper import fetch_jobs
from utils import is_duplicate

import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=5
)

TOPIC = "jobs_topic"

def get_mock_jobs():
    roles = ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer", "DevOps Engineer"]
    skills = [
        ["Python", "SQL"],
        ["Python", "Machine Learning"],
        ["Python", "Java", "SQL", "AWS", "Docker", "Kubernetes"],
        ["Python", "JavaScript", "React", "Node.js"],
        ["Python", "AWS", "Docker", "Kubernetes"]
    ]

    return {
        "title": random.choice(roles),
        "company": f"DemoCorp",
        "location": "Remote",
        "skills": random.choice(skills),
        "timestamp": time.time()
    }

def send_to_kafka(job):
    try:
        producer.send(TOPIC, job)
        producer.flush()
        print(f"Sent job: {job['title']} at {job['company']}")
    except Exception as e:
        print(f"Kafka send failed: {e}")

def run():
    while True:
        jobs = fetch_jobs()
        
        if not jobs:
            print("Scrapped failed, using Mock data...")
            jobs = [get_mock_jobs() for _ in range(5)]
            # time.sleep(10)
            # continue
        
        for job in jobs:
            if is_duplicate(job):
                continue
            
            send_to_kafka(job)
        
        time.sleep(30)

if __name__ == "__main__":
    run()