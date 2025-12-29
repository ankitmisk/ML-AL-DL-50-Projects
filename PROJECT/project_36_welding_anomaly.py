PROJECT = {
    "name": "Welding Anomaly Detection",
    "icon": "🔥",
    "dataset": "Welding Sensor Signals",
    "description": "Detect abnormal welding patterns using Isolation Forest.",
    "steps": "Extract Features → Isolation Forest → Anomaly Scores",
    "code": """
import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("weld_signals.csv")

model = IsolationForest(contamination=0.05)
model.fit(df)

scores = model.decision_function(df)
outliers = model.predict(df)

print(outliers[:20])
"""
}
