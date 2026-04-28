from kafka import KafkaConsumer
import json
from etl import clean_job
from db_postgres import insert_job
from db_mongo import insert_raw

consumer = KafkaConsumer(
    'jobs_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def run():
    for message in consumer:
        raw_job = message.value

        try:
            # Store raw data (Mongo)
            insert_raw(raw_job)

            # Clean data
            clean = clean_job(raw_job)

            # Store structured data (Postgres)
            insert_job(clean)

            print("Processed:", clean["title"])

        except Exception as e:
            print("Processing error:", e)


if __name__ == "__main__":
    run()