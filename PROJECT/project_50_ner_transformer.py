PROJECT = {
    "name": "Named Entity Recognition (NER)",
    "icon": "🔍",
    "dataset": "CoNLL 2003",
    "description": "Detect Persons, Organizations, Locations using Transformer NER.",
    "steps": "Load Model → Predict Entities → Display Labels",
    "code": """
from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

text = "Elon Musk is the CEO of Tesla based in California."

print(ner(text))
"""
}
