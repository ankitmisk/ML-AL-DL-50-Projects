PROJECT = {
    "name": "Sales Forecasting (LSTM)",
    "icon": "📈",
    "dataset": "Retail sales CSV",
    "description": "Predict future sales using LSTM deep learning.",
    "steps": "Sequence → LSTM → Predict",
    "code": """
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv("sales.csv")
sales = df["Sales"].values.reshape(-1,1)

sc = MinMaxScaler()
scaled = sc.fit_transform(sales)

X, y = [], []
for i in range(30, len(scaled)):
    X.append(scaled[i-30:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(30,1)),
    LSTM(32),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=5)

model.save("sales_lstm.h5")
"""
}
