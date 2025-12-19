from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
model = SentenceTransformer('all-MiniLM-L6-v2')


# 👇 This was missing
class MatchRequest(BaseModel):
    resume: str
    job: str


def classify_match(score):
    if score >= 0.75:
        return "Excellent Match"
    elif score >= 0.55:
        return "Good Match"
    elif score >= 0.40:
        return "Average Match"
    else:
        return "Poor Match"


@app.post("/match")
def match_resume(data: MatchRequest):
    resume_vec = model.encode([data.resume])
    job_vec = model.encode([data.job])

    score = cosine_similarity(resume_vec, job_vec)[0][0]

    return {
        "match_percentage": round(score * 100, 2),
        "match_level": classify_match(score)
    }
