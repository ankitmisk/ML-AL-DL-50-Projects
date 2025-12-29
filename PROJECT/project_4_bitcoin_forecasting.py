PROJECT = {
    "name": "Bitcoin Price Prediction (LSTM)",
    "icon": "🪙",
    "dataset": "Yahoo Finance BTC-USD",
    "description": "Forecast Bitcoin using LSTM neural network.",
    "steps": "Sequence → Normalize → LSTM → Predict",
    "code": """
import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = yf.download("BTC-USD", start="2014-01-01")

close = df["Close"].values.reshape(-1, 1)

sc = MinMaxScaler()
scaled = sc.fit_transform(close)

X, y = [], []

for i in range(60, len(scaled)):
    X.append(scaled[i-60:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(60,1)),
    LSTM(64),
    Dense(1)
])

model.compile(loss="mse", optimizer="adam")
model.fit(X, y, epochs=6)

model.save("btc_lstm_model.h5")
"""
}
