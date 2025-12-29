PROJECT = {
    "name": "Image Caption Generator (CNN + LSTM)",
    "icon": "🖼️",
    "dataset": "Flickr8k",
    "description": "Generate captions for images using CNN encoder + LSTM decoder.",
    "steps": "Extract features → Train LSTM → Predict captions",
    "code": """
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
import numpy as np

vgg = VGG16()
model = Model(inputs=vgg.inputs, outputs=vgg.layers[-2].output)

img = load_img("example.jpg", target_size=(224,224))
img = img_to_array(img)
img = img.reshape((1,224,224,3))

features = model.predict(img)
print("Image features shape:", features.shape)

print("Caption generation model placeholder (training requires dataset)")
"""
}
