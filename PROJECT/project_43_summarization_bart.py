PROJECT = {
    "name": "Text Summarization (BART)",
    "icon": "📝",
    "dataset": "CNN/DailyMail",
    "description": "Generate abstractive summaries using BART transformers.",
    "steps": "Load BART → Pass Text → Get Summary",
    "code": """
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = \"\"\"India is one of the fastest-growing digital economies...\"\"\"

summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
print(summary[0]["summary_text"])
"""
}
