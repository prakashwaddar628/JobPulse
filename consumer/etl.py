def normalize_text(text):
    """
    Normalize the input text by converting it to lowercase and stripping leading/trailing whitespace.
    
    Args:
        text (str): The input text to be normalized.
        
    Returns:
        str: The normalized text.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    
    return text.strip().title()

def normalize_skills(skills):
    mapping = {
        "python": "Python",
        "ml": "Machine Learning",
        "ai": "Artificial Intelligence"
    }

    normalized = []

    for skill in skills:
        skill_lower = skill.lower()
        normalized.append(mapping.get(skill_lower, skill.title()))
        
    return list(set(normalized))

def clean_job(job):
    return {
        "title": normalize_text(job.get("title", "")),
        "company": normalize_text(job.get("company", "")),
        "location": normalize_text(job.get("location", "")),
        "skills": normalize_skills(job.get("skills", []))
    }