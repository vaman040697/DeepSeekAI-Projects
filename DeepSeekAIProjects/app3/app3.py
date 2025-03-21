from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/correct/")
def correct_grammar(text:str):
    payload = {"model": "deepseek-r1", "prompt": f"Correct grammar:\n\n{text}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No content generated.")

#uvicorn app:app --reload