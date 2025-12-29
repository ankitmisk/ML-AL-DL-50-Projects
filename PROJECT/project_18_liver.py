PROJECT = {
    "name": "Liver Disease Prediction",
    "icon": "🧫",
    "dataset": "Liver Patient Dataset",
    "description": "Predict liver disease using SVM.",
    "steps": "Clean → Encode → Train",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

df = pd.read_csv("liver.csv").dropna()

X = df.drop("Liver_Disease", axis=1)
y = df["Liver_Disease"]

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = SVC(kernel="rbf")
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
