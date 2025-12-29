PROJECT = {
    "name": "Topic Modeling (LDA)",
    "icon": "🧩",
    "dataset": "Custom Text Corpus",
    "description": "Extract topics from text using Latent Dirichlet Allocation.",
    "steps": "Clean → Tokenize → Build LDA → Show Topics",
    "code": """
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv("corpus.csv")

cv = CountVectorizer(stop_words="english")
mat = cv.fit_transform(df["text"])

lda = LatentDirichletAllocation(n_components=5)
lda.fit(mat)

words = cv.get_feature_names_out()

for idx, comp in enumerate(lda.components_):
    terms = [words[i] for i in comp.argsort()[-10:]]
    print(f"Topic {idx+1}: ", " ".join(terms))
"""
}
