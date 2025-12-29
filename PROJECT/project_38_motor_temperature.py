PROJECT = {
    "name": "Motor Temperature Prediction",
    "icon": "🌡️",
    "dataset": "Electric Motor Temperature",
    "description": "Predict motor temperature using RandomForestRegressor.",
    "steps": "Train → Predict → MAE",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("motor_temp.csv")

X = df.drop("temp",axis=1)
y = df["temp"]

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = RandomForestRegressor()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("MAE =",mean_absolute_error(y_test,pred))
"""
}
