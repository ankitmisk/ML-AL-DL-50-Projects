PROJECT = {
    "name": "Financial Risk Scoring Model",
    "icon": "📊",
    "dataset": "Bank Loan Risk",
    "description": "Score customers using Logistic Regression.",
    "steps": "Clean → Train → Score",
    "code": """
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("risk_data.csv").dropna()

X = df.drop("default", axis=1)
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
