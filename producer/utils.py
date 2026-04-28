import hashlib

seen_jobs = set()

def generate_job_id(job):
    unique_str = f"{job['title']}_{job['company']}_{job['location']}"
    return hashlib.md5(unique_str.encode()).hexdigest()

def is_duplicate(job):
    job_id = generate_job_id(job)

    if job_id in seen_jobs:
        return True
    
    seen_jobs.add(job_id)
    return False