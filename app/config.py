from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL")
