PROJECT = {
    "name": "Inventory Stockout Prediction",
    "icon": "📦",
    "dataset": "Inventory CSV",
    "description": "Predict which products will go out of stock.",
    "steps": "Clean → RF Classifier → Predict",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("inventory.csv").fillna(0)

X = df.drop("stockout", axis=1)
y = df["stockout"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print(classification_report(y_test,pred))
"""
}
