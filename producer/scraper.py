import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_jobs():
    url = "https://in.indeed.com/jobs?q=python+developer&l=Bangalore"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job_card in soup.select(".job_seen_beacon"):
        try:
            title = job_card.select_one("h2").text.strip()
            company = job_card.select_one(".companyName").text.strip()
            location = job_card.select_one(".companyLocation").text.strip()

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "skills": extract_skills(title),
                "timestamp": time.time()
            })

        except Exception:
            continue
        
    return jobs

def extract_skills(text):
    SKILLS = ["Python", "SQL", "Machine Learning", "Django", "AWS"]

    found = []
    text_lower = text.lower()

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found.append(skill)
    
    return found