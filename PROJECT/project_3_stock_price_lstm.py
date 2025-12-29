PROJECT = {
    "name": "Stock Price Forecasting (LSTM)",
    "icon": "📈",
    "dataset": "Yahoo Finance",
    "description": "Predict next-day closing prices using LSTM.",
    "steps": """
    1. Download stock data  
    2. Normalize close price  
    3. Create 60-day sequences  
    4. Build LSTM model  
    5. Train & predict  
    """,
    "code": """
import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = yf.download("AAPL", start="2010-01-01", end="2023-01-01")

prices = df["Close"].values.reshape(-1, 1)

sc = MinMaxScaler()
scaled = sc.fit_transform(prices)

X, y = [], []
for i in range(60, len(scaled)):
    X.append(scaled[i - 60:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(60, 1)),
    LSTM(32),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=5)

model.save("stock_model_lstm.h5")
"""
}
