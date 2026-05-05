from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from api.db import cursor
from ml.anomaly import detect_anomalies

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "JobPulse API is running!"}

@app.get("/jobs")
def get_jobs():
    cursor.execute("SELECT title, company, location, skills FROM jobs ORDER BY id DESC LIMIT 50;")
    rows = cursor.fetchall()

    jobs = []
    for row in rows:
        jobs.append({
            "title": row[0],
            "company": row[1],
            "location": row[2],
            "skills": row[3]
        })

    return {"jobs": jobs}

@app.get("/skills")
def get_skills():
    cursor.execute("SELECT skills from jobs")
    rows = cursor.fetchall()

    skill_count = {}

    for row in rows:
        for skill in row[0]:
            skill_count[skill] = skill_count.get(skill, 0) + 1
    
    return detect_anomalies(skill_count)