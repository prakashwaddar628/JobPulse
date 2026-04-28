import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = conn.cursor()

def insert_job(job):
    try:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, skills)
            VALUES (%s, %s, %s, %s
            )""", (
                job['title'], 
                job['company'], 
                job['location'], 
                job['skills']
        ))
        conn.commit()
    except Exception as e:
        print(f"PostgreSQL Error: {e}")
        conn.rollback()