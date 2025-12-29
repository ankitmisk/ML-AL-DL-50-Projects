PROJECT = {
    "name": "Breast Cancer Classification",
    "icon": "🎀",
    "dataset": "sklearn breast_cancer",
    "description": "Classify malignant vs benign tumors.",
    "steps": """
    1. Load sklearn dataset
    2. Create train/test split
    3. Train RandomForest
    4. Evaluate model accuracy
    """,
    "code": """
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
