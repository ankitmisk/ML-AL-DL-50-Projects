PROJECT = {
    "name": "Insurance Claim Prediction",
    "icon": "🧾",
    "dataset": "Insurance.csv",
    "description": "Predict whether a customer will file a claim.",
    "steps": "Clean → Encode → Train → Predict",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("insurance.csv").fillna(0)

X = df.drop("made_claim", axis=1)
y = df["made_claim"]

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
