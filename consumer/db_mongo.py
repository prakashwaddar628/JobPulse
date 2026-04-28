from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["jobpulse"]
collection = db["jobs_raw"]

def insert_raw(job):
    try:
        collection.insert_one(job)
    except Exception as e:
        print(f"MongoDB Error: {e}")