from kafka import KafkaProducer
import json
import time
from scraper import fetch_jobs
from utils import is_duplicate

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=5
)

TOPIC = "jobs_topic"

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
            print("No jobs found, retrying in 60 seconds...")
            time.sleep(10)
            continue
        
        for job in jobs:
            if is_duplicate(job):
                continue
            
            send_to_kafka(job)
        
        time.sleep(30)

if __name__ == "__main__":
    run()