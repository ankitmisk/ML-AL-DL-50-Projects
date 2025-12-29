PROJECT = {
    "name": "Customer Lifetime Value (CLV)",
    "icon": "💳",
    "dataset": "Olist E-commerce",
    "description": "Predict CLV using Gradient Boosting Regression.",
    "steps": "Feature engineering → Train → Predict",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv("clv.csv")

X = df.drop("clv", axis=1)
y = df["clv"]

X_train, X_test, y_train, y_test = train_test_split(X,y)

model = GradientBoostingRegressor()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("RMSE =", mean_squared_error(y_test,pred)**0.5)
"""
}
