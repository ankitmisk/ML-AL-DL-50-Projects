PROJECT = {
    "name": "Kidney Disease Detection",
    "icon": "🧪",
    "dataset": "Kidney Disease CSV",
    "description": "Predict CKD using RandomForest.",
    "steps": "Clean → Encode → Train",
    "code": """
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("kidney.csv").fillna(0)

for col in df.select_dtypes("object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("classification", axis=1)
y = df["classification"]

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
