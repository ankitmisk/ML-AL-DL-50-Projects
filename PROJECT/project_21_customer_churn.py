PROJECT = {
    "name": "Customer Churn Prediction",
    "icon": "🚪",
    "dataset": "Kaggle → Telco Customer Churn",
    "description": "Predict customer churn using Logistic Regression.",
    "steps": """
    1. Load Telco dataset  
    2. Clean missing values  
    3. Label encode categorical columns  
    4. Scale features  
    5. Train Logistic Regression  
    6. Evaluate results  
    """,
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("telco.csv").fillna("Unknown")

# Encode
for col in df.select_dtypes("object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
