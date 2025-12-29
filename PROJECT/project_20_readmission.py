PROJECT = {
    "name": "Hospital Readmission Prediction",
    "icon": "🏥",
    "dataset": "UCI Diabetes Readmission Dataset",
    "description": "Predict 30-day readmissions.",
    "steps": "Clean → Encode → Train → Predict",
    "code": """
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("readmission.csv").fillna("Unknown")

for col in df.select_dtypes("object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("readmitted", axis=1)
y = df["readmitted"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = GradientBoostingClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
