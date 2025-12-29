PROJECT = {
    "name": "Question Answering (BERT)",
    "icon": "❓",
    "dataset": "SQuAD v2",
    "description": "Answer questions from context using BERT QA pipeline.",
    "steps": "Load BERT → Ask Question → Get Answer",
    "code": """
from transformers import pipeline

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

context = \"\"\"The Taj Mahal is located in Agra, India...\"\"\"

result = qa({
    "question": "Where is Taj Mahal located?",
    "context": context
})

print(result)
"""
}
