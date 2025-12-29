PROJECT = {
    "name": "Machine Translation (English → German)",
    "icon": "🌍",
    "dataset": "HuggingFace → Helsinki-NLP",
    "description": "Translate English text to German using MarianMT.",
    "steps": "Load MarianMT → Translate → Output German",
    "code": """
from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-en-de"
tok = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = ["I love machine learning"]

tokens = tok(text, return_tensors="pt", padding=True)
translated = model.generate(**tokens)

print(tok.decode(translated[0], skip_special_tokens=True))
"""
}
