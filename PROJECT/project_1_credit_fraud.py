PROJECT = {
    "name": "Credit Card Fraud Detection",
    "icon": "🚨",
    "dataset": "Kaggle → https://www.kaggle.com/mlg-ulb/creditcardfraud",
    "description": "Detect fraudulent credit card transactions using SMOTE + RandomForest.",
    "steps": """
    1. Load imbalanced creditcard.csv dataset  
    2. Separate X and y  
    3. Apply SMOTE oversampling  
    4. Train RandomForest  
    5. Generate classification report  
    """,
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

sm = SMOTE()
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

model = RandomForestClassifier()
model.fit(X_train_res, y_train_res)

pred = model.predict(X_test)

print("\\nClassification Report:\\n")
print(classification_report(y_test, pred))
"""
}
