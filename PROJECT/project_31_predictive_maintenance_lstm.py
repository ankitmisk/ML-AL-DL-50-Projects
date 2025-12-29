PROJECT = {
    "name": "Predictive Maintenance (LSTM)",
    "icon": "⚙️",
    "dataset": "NASA Turbofan CMAPSS",
    "description": "Predict Remaining Useful Life (RUL) of engines using LSTM.",
    "steps": """
    1. Load CMAPSS dataset
    2. Normalize sensor features
    3. Create time sequences
    4. Train LSTM to predict RUL
    """,
    "code": """
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv("train_FD001.txt", sep=" ", header=None).dropna(axis=1)
df.columns = ["unit","time"] + [f"s{i}" for i in range(1,23)]

df["RUL"] = df.groupby("unit")["time"].transform(lambda x: x.max() - x)

features = df.drop(["unit","RUL"], axis=1).values
labels = df["RUL"].values

sc = MinMaxScaler()
features = sc.fit_transform(features)

X, y = [], []
window = 30

for i in range(window, len(features)):
    X.append(features[i-window:i])
    y.append(labels[i])

X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(window, X.shape[2])),
    LSTM(32),
    Dense(1)
])

model.compile(loss="mse", optimizer="adam")
model.fit(X, y, epochs=5)

model.save("predictive_maintenance_lstm.h5")
"""
}
