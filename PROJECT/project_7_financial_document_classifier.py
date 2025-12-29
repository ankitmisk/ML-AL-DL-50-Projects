PROJECT = {
    "name": "Financial Document Classifier",
    "icon": "📄",
    "dataset": "PDF → Text extracted",
    "description": "Classify financial documents using TF-IDF + SVM.",
    "steps": "Extract text → TFIDF → SVM",
    "code": """
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("finance_docs.csv")

tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["text"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = SVC(kernel="linear")
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
