from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#loaded pre-trained BERT model

model = SentenceTransformer('all-MiniLM-L6-v2')

resume = "Java developer with spring Boot and Mysql experience "
job_description = "Looking for the backend developer with skilled in java and spring "


#convert text into vectors
resume_embedding = model.encode([resume])
job_embedding = model.encode([job_description])

def clean_text(text):
    return text.lower().strip()
def get_match_percentage(score):
    return round(score * 100, 2)


# Calculate similarity
similarity = cosine_similarity(resume_embedding, job_embedding)

print("Match Score:", similarity[0][0])
