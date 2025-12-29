PROJECT = {
    "name": "Revenue Prediction (Regression)",
    "icon": "💰",
    "dataset": "Retail Store Revenue CSV",
    "description": "Predict store weekly revenue using regression.",
    "steps": "Train/Test → Regression → Predict",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("revenue.csv").fillna(0)

X = df.drop("Revenue", axis=1)
y = df["Revenue"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("MAE =", mean_absolute_error(y_test,pred))
"""
}
