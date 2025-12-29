PROJECT = {
    "name": "Casting Defect Detection",
    "icon": "🏗️",
    "dataset": "Casting Product Images",
    "description": "CNN model for detecting defective castings.",
    "steps": "Image Augmentation → CNN → Train",
    "code": """
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

train = ImageDataGenerator(rescale=1/255).flow_from_directory(
    "casting/train", target_size=(128,128), class_mode="binary"
)

model = Sequential([
    Conv2D(32,(3,3),activation="relu",input_shape=(128,128,3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128,activation="relu"),
    Dense(1,activation="sigmoid")
])

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model.fit(train,epochs=3)
"""
}
