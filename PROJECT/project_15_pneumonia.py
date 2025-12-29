PROJECT = {
    "name": "Pneumonia Detection (CNN)",
    "icon": "🫁",
    "dataset": "Chest X-ray Pneumonia Dataset",
    "description": "Classify pneumonia vs normal using MobileNetV2 transfer learning.",
    "steps": "Transfer Learning → Train → Evaluate",
    "code": """
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense

train = ImageDataGenerator(rescale=1/255).flow_from_directory(
    "chest_xray/train", target_size=(224,224), class_mode="binary"
)

test = ImageDataGenerator(rescale=1/255).flow_from_directory(
    "chest_xray/test", target_size=(224,224), class_mode="binary"
)

base = MobileNetV2(weights="imagenet", include_top=False)
base.trainable = False

model = Sequential([
    base,
    GlobalAveragePooling2D(),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(train, epochs=3)
"""
}
