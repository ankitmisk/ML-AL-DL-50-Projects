PROJECT = {
    "name": "E-commerce Sentiment Analysis",
    "icon": "💬",
    "dataset": "Amazon Reviews",
    "description": "Classify sentiment of customer reviews.",
    "steps": "Clean → TFIDF → NB Classifier",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

df = pd.read_csv("amazon_sentiment.csv").dropna()

tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["review"])
y = df["label"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = MultinomialNB()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
