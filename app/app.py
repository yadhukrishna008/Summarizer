from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from app.schema import SummarizeRequest, SummarizeResponse, prompt_template
from app.config import OLLAMA_HOST_URL


if not OLLAMA_HOST_URL:
    raise RuntimeError("OLLAMA_HOST_URL is not set in .env")

app= FastAPI()

# Configure CORS (allows frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/summarize", response_model= SummarizeResponse)
async def summarize_text(request: SummarizeRequest):
    prompt = prompt_template.replace("{TEXT}", request.text)

    res = requests.post(
        OLLAMA_HOST_URL,
        json={
            "model": "llama3:latest",
            "prompt": prompt,
            "stream": False
        })

    data = res.json().strip()
    if "response" not in data:
        raise RuntimeError(f"Unexpected Ollama response: {data}")
        
    return {"summaries" : data["response"]}

