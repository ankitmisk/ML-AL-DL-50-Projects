PROJECT = {
    "name": "Spam Email Classifier",
    "icon": "📩",
    "dataset": "SMS Spam Collection",
    "description": "Classify SMS as spam or ham using TF-IDF + Naive Bayes.",
    "steps": "Clean → TFIDF → NB → Evaluate",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

df = pd.read_csv("spam.csv", encoding="latin-1")
df = df[["v1", "v2"]]
df.columns = ["label", "text"]
df["label"] = df["label"].map({"ham": 0, "spam": 1})

tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["text"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = MultinomialNB()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
