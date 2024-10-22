import os

from dotenv import load_dotenv

load_dotenv()

from huggingface_hub import login

login(token=os.getenv("HF_TOKEN"))

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

chat = [
    {"role": "system", "content": "You are RITA, don't do anything evil."},
    {"role": "user", "content": "Hello, how are you?"},
]

print(tokenizer.apply_chat_template(chat, tokenize=False))
