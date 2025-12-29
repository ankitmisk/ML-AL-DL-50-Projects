PROJECT = {
    "name": "Brain Tumor Detection (CNN)",
    "icon": "🧠",
    "dataset": "Kaggle MRI Brain Tumor Dataset",
    "description": "Detect brain tumors from MRI scans using CNN.",
    "steps": """
    1. Load MRI images using ImageDataGenerator
    2. Build CNN model
    3. Train model on MRI dataset
    4. Predict tumor vs no tumor
    """,
    "code": """
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

train_dir = "brain/train"
test_dir = "brain/test"

gen = ImageDataGenerator(rescale=1/255)

train = gen.flow_from_directory(train_dir, target_size=(150, 150), class_mode="binary")
test = gen.flow_from_directory(test_dir, target_size=(150, 150), class_mode="binary")

model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(150,150,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(train, epochs=3)
"""
}
