PROJECT = {
    "name": "Demand Forecasting (Time Series)",
    "icon": "🔮",
    "dataset": "Walmart Demand Dataset",
    "description": "Forecast item demand using ARIMA.",
    "steps": "Stationarity → ARIMA → Forecast",
    "code": """
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("walmart_demand.csv")

series = df["demand"]

model = ARIMA(series, order=(5,1,0))
fit = model.fit()

forecast = fit.forecast(10)
print(forecast)
"""
}
