PROJECT = {
    "name": "Dynamic Pricing Model",
    "icon": "🏷️",
    "dataset": "Pricing Dataset",
    "description": "Estimate optimal price using elasticity-based regression.",
    "steps": "Clean → Regression → Elasticity → Optimal price",
    "code": """
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pricing.csv")

X = df[["price"]]
y = df["units_sold"]

model = LinearRegression()
model.fit(X, y)

elasticity = (model.coef_[0] * df["price"].mean()) / df["units_sold"].mean()

optimal_price = df["price"].mean() * (1 + elasticity)

print("Elasticity =", elasticity)
print("Optimal Price =", optimal_price)
"""
}
