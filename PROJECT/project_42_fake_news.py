PROJECT = {
    "name": "Fake News Detection",
    "icon": "📰",
    "dataset": "Kaggle Fake News",
    "description": "Classify fake vs real news using TF-IDF + Logistic Regression.",
    "steps": "Clean → Vectorize → Train → Evaluate",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("fake_news.csv").dropna()

tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
X = tfidf.fit_transform(df["text"])
y = df["label"].map({"FAKE": 1, "REAL": 0})

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
