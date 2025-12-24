FastAPI Text Summarizer

A simple FastAPI-based REST API that summarizes input text using pre-set prompt, powered by a local LLaMA 3 model via Ollama. This project was built for learning purposes to understand FastAPI, request/response validation, prompt engineering, and local LLM integration.

How It Works?
Client sends text to the /summarize endpoint
Prompt is sent to the local LLaMA 3 model
The API return summary

Tech Stack:
Python 3.10+
FastAPI – API framework
Uvicorn – ASGI server
Pydantic – Request/response validation
Ollama – Local LLM runtime
LLaMA 3 – Language model
Requests – HTTP client for Ollama
CORS Middleware – Browser access support

Prerequisites:
Python installed
Ollama installed (ttps://ollama.com)
LLaMA 3 model downloaded:(ollama pull llama3)



