PROJECT = {
    "name": "Energy Consumption Forecasting",
    "icon": "⚡",
    "dataset": "Household Power Consumption Dataset",
    "description": "Predict energy usage using LSTM.",
    "steps": "Preprocess → Scale → LSTM → Predict",
    "code": """
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv("energy.csv")
series = df["power"].values.reshape(-1,1)

sc = MinMaxScaler()
scaled = sc.fit_transform(series)

X, y = [], []
for i in range(24, len(scaled)):
    X.append(scaled[i-24:i])
    y.append(scaled[i])

X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(24,1)),
    LSTM(32),
    Dense(1)
])

model.compile(optimizer="adam", loss="mse")
model.fit(X,y,epochs=5)

model.save("energy_lstm.h5")
"""
}
