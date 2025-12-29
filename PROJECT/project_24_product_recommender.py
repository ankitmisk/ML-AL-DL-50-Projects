PROJECT = {
    "name": "Product Recommendation System",
    "icon": "🎁",
    "dataset": "Amazon Reviews JSON",
    "description": "Content-based recommendation using TF-IDF similarity.",
    "steps": "Clean → TFIDF → Cosine Similarity → Recommend",
    "code": """
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_json("amazon_reviews.json", lines=True)
df = df[["title", "reviewText"]].dropna()
df["text"] = df["title"] + " " + df["reviewText"]

tfidf = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(df["text"])

sim = cosine_similarity(matrix)

def recommend(idx):
    scores = sim[idx]
    top = scores.argsort()[-6:-1]
    return df.iloc[top]["title"]

print(recommend(10))
"""
}
