PROJECT = {
    "name": "Medical Cost Prediction",
    "icon": "💵",
    "dataset": "Medical Insurance Cost Dataset",
    "description": "Predict medical costs using Linear Regression.",
    "steps": "Encode → Train → Predict",
    "code": """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("insurance.csv")

X = df.drop("charges", axis=1)
y = df["charges"]

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), ["sex","smoker","region"])],
    remainder="passthrough"
)

X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)

pred = model.predict(X_test)
print("MAE =", mean_absolute_error(y_test,pred))
"""
}
