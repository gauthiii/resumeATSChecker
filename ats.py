import spacy
from docx import Document

# Define career-related keywords
career_keywords = {
    "skills": {
        "python", "java", "c", "c++", "c#", "r", "sql", "javascript", "typescript", "go", "kotlin", "swift", "bash",
        "html", "css", "sass", "scala", "ruby", "php", "perl", "matlab", "tensorflow", "keras", "pytorch", "scikit-learn",
        "pandas", "numpy", "matplotlib", "seaborn", "plotly", "d3.js", "tableau", "power bi", "excel", "git", "github",
        "docker", "kubernetes", "jenkins", "ansible", "aws", "azure", "gcp", "salesforce", "oracle", "sap", "hadoop",
        "spark", "airflow", "databricks", "flask", "django", "node.js", "react", "angular", "vue.js", "svelte",
        "bootstrap", "tailwind", "json", "xml", "api", "sql", "no-sql", "mongodb", "firebase", "elasticsearch",
        "terraform", "bigquery", "apache", "nginx", "networking", "linux", "windows", "macos", "android", "ios",
        "computer architecture", "operating systems", "generative ai"
    },
    "technologies": {
        "ai", "artificial intelligence", "machine learning", "deep learning", "computer vision", "natural language processing",
        "nlp", "speech recognition", "recommendation systems", "time series analysis", "predictive analytics", 
        "big data", "cloud computing", "data science", "data engineering", "cybersecurity", "blockchain", "fintech",
        "devops", "augmented reality", "virtual reality", "ar", "vr", "metaverse", "internet of things", "iot",
        "edge computing", "quantum computing", "mobile development", "web development", "e-commerce", "business intelligence"
    },
    "roles": {
        "developer", "engineer", "scientist", "analyst", "intern", "internship", "manager", "consultant", "architect",
        "administrator", "specialist", "coordinator", "tester", "trainer", "data engineer", "machine learning engineer",
        "software developer", "full-stack developer", "front-end developer", "back-end developer", "devops engineer",
        "security analyst", "cloud architect", "technical lead", "product manager", "project manager", "systems analyst"
    },
    "qualifications": {
        "bachelor", "master", "phd", "mba", "btech", "mtech", "degree", "certified", "certifications", "diploma",
        "associate", "professional", "certified scrum master", "aws certified", "pmp", "cissp", "ccna", "ccnp",
        "microsoft certified", "oracle certified", "google certified", "professional engineer", "cs degree",
        "engineering degree", "statistics degree", "mathematics degree", "economics degree", "computer science"
    },
    "tools": {
        "api", "sdk", "frameworks", "jupyter", "firebase", "google colab", "docker", "kubernetes", "jenkins",
        "ansible", "terraform", "tableau", "power bi", "hadoop", "spark", "airflow", "databricks", "flask", "django",
        "numpy", "pandas", "matplotlib", "scikit-learn", "pytorch", "tensorflow", "keras", "vscode", "intellij",
        "eclipse", "android studio", "xcode", "git", "github", "gitlab", "bitbucket", "jira", "confluence", "trello",
        "asana", "microsoft project", "notion", "postman", "swagger", "selenium", "appium", "cucumber"
    }
}

# Combine all career-related keywords into a single set
all_career_keywords = set()
for category in career_keywords.values():
    all_career_keywords.update(category)

def extract_text_from_docx(file_path):
    """Extract text from a .docx file."""
    doc = Document(file_path)
    return " ".join([p.text for p in doc.paragraphs])

def extract_keywords(text):
    """Extract keywords from a given text using spaCy and filter with career-related keywords."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    keywords = {token.text.lower() for token in doc if token.is_alpha and not token.is_stop}
    # Filter keywords to include only career-related terms
    filtered_keywords = keywords.intersection(all_career_keywords)
    return filtered_keywords

def calculate_similarity(resume_keywords, job_keywords):
    """Calculate similarity score between resume and job keywords."""
    matches = resume_keywords.intersection(job_keywords)
    score = len(matches) / len(job_keywords) * 100 if job_keywords else 0
    return round(score, 2), matches

def analyze_resume(resume_path, job_description):
    """Analyze resume against the job description."""
    resume_text = extract_text_from_docx(resume_path)
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    
    score, matches = calculate_similarity(resume_keywords, job_keywords)
    print("***********************************")
    print("Resume Key: ", resume_keywords)
    print("Job Key: ", job_keywords)
    print("***********************************")
    return {
        "score": score,
        "matches": matches,
        "total_job_keywords": len(job_keywords),
        "total_resume_keywords": len(resume_keywords),
    }

# Example Usage
if __name__ == "__main__":
    resume_file = "Gautham_Resume_ML_AI.docx"
    job_desc = """
    - Currently enrolled in, or completed a Bachelor’s degree program or higher in Computer Science, Computer Engineering, Electrical Engineering or related field - To qualify, applicants should have earned a Bachelor’s or Master’s degree between May 2023 to September 2025. Possible start dates for this role are between January 2025 to October 2025. - Programming experience in internship or coursework with programming language such as Python and/or C or C++. Candidates with strong interests and academic qualifications/research focus in two of the following: - Distributed systems, algorithms (MPI, NCCL, or similar) - Operating System - Linux system programming/services - Computer architecture - System Development - Complexity analysis
    """

    result = analyze_resume(resume_file, job_desc)
    print(f"Resume Score: {result['score']}%")
    print(f"Matching Keywords: {', '.join(result['matches'])}")
    print(f"Total Job Keywords: {result['total_job_keywords']}")
    print(f"Total Resume Keywords: {result['total_resume_keywords']}")
