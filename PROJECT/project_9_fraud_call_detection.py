PROJECT = {
    "name": "Fraud Call Detection",
    "icon": "📞",
    "dataset": "Call Log CSV",
    "description": "Detect fraudulent calls using RandomForest.",
    "steps": "Feature extraction → Train → Predict",
    "code": """
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

df = pd.read_csv("call_logs.csv")

X = df.drop("fraud", axis=1)
y = df["fraud"]

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
