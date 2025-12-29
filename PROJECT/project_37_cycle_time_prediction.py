PROJECT = {
    "name": "Assembly Line Cycle Time Prediction",
    "icon": "⏱️",
    "dataset": "Cycle Time CSV",
    "description": "Predict assembly cycle time using Gradient Boosting.",
    "steps": "Feature Eng → Train → MAE",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("cycle_time.csv")

X = df.drop("cycle_time",axis=1)
y = df["cycle_time"]

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = GradientBoostingRegressor()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("MAE =", mean_absolute_error(y_test,pred))
"""
}
