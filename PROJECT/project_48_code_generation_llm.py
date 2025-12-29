PROJECT = {
    "name": "Code Generation LLM",
    "icon": "💻",
    "dataset": "BigCode / StarCoder",
    "description": "Generate Python code using a pretrained CodeGen model.",
    "steps": "Load Model → Provide Prompt → Generate Code",
    "code": """
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "bigcode/starcoder"
tok = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Write a Python function to check prime numbers."

inputs = tok(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=150)

print(tok.decode(outputs[0], skip_special_tokens=True))
"""
}
