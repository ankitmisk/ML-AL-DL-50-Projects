PROJECT = {
    "name": "Heart Disease Prediction",
    "icon": "❤️",
    "dataset": "UCI Heart Disease Dataset",
    "description": "Predict whether a patient has heart disease.",
    "steps": """
    1. Load heart dataset
    2. Split features/labels
    3. Train Logistic Regression
    4. Evaluate classification metrics
    """,
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("heart.csv")

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
