PROJECT = {
    "name": "Anomaly Detection (Autoencoder)",
    "icon": "❗",
    "dataset": "MVTec AD",
    "description": "Detect manufacturing anomalies using autoencoder reconstruction error.",
    "steps": "Train AE → Compute Reconstruction Error → Flag Outliers",
    "code": """
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

data = np.load("normal_images.npy") / 255.0

model = models.Sequential([
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(64, activation="relu"),
    layers.Dense(128, activation="relu"),
    layers.Dense(data.shape[1]*data.shape[2]*data.shape[3], activation="sigmoid"),
    layers.Reshape(data.shape[1:])
])

model.compile(optimizer="adam", loss="mse")
model.fit(data, data, epochs=5)

test = np.load("test_images.npy") / 255.0
recon = model.predict(test)

error = np.mean((recon - test)**2, axis=(1,2,3))
print(error[:10])
"""
}
