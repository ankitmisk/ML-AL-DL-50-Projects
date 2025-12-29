PROJECT = {
    "name": "Diabetes Prediction",
    "icon": "🩺",
    "dataset": "Kaggle → PIMA Diabetes Dataset",
    "description": "Predict onset of diabetes using RandomForest.",
    "steps": """
    1. Load diabetes dataset
    2. Split into train/test
    3. Standardize numeric columns
    4. Train RandomForestClassifier
    5. Evaluate using classification report
    """,
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("diabetes.csv")

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
