import requests
from bs4 import BeautifulSoup
import random
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def fetch_jobs():
    url = "https://remoteok.com/remote-python-jobs"

    for attempt in range(3):
        try:
            session = requests.Session()
            session.headers.update(HEADERS)

            time.sleep(random.uniform(2, 5))

            response = session.get(url, timeout=10)

            if response.status_code == 403:
                print("Blocked! Retrying...")
                time.sleep(5)
                continue

            response.raise_for_status()
            break

        except Exception as e:
            print(f"Attempt {attempt+1} failed:", e)
            time.sleep(5)
    else:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job_card in soup.select(".job_seen_beacon"):
        try:
            title = job_card.select_one("h2")
            company = job_card.select_one(".companyName")
            location = job_card.select_one(".companyLocation")

            if not title or not company or not location:
                continue

            job = {
                "title": title.text.strip(),
                "company": company.text.strip(),
                "location": location.text.strip(),
                "skills": extract_skills(title.text),
                "timestamp": time.time()
            }

            jobs.append(job)

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