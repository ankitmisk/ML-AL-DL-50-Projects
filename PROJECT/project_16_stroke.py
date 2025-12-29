PROJECT = {
    "name": "Stroke Prediction",
    "icon": "🧠",
    "dataset": "Kaggle Stroke Dataset",
    "description": "Predict stroke risk using ML classifier.",
    "steps": "Clean → Encode → Train → Predict",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("stroke.csv").dropna()

for col in df.select_dtypes("object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("stroke", axis=1)
y = df["stroke"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
