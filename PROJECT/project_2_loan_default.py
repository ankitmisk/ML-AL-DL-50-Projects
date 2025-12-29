PROJECT = {
    "name": "Loan Default Prediction",
    "icon": "🏦",
    "dataset": "Kaggle Lending Club",
    "description": "Predict if a loan will default using Logistic Regression.",
    "steps": """
    1. Load Lending Club dataset  
    2. Clean & select relevant features  
    3. Label encode strings  
    4. Standardize numeric values  
    5. Train Logistic Regression  
    6. Evaluate  
    """,
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("loan.csv").dropna()

df["loan_status"] = df["loan_status"].apply(
    lambda x: 1 if "Charged Off" in x else 0
)

df["emp_length"] = LabelEncoder().fit_transform(df["emp_length"])

X = df.drop("loan_status", axis=1)
y = df["loan_status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = LogisticRegression(max_iter=300)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
"""
}
