from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
api_key = os.getenv("GEMINI_API_KEY")
api_url = os.getenv("API_URL")

# if not api_key:
#     raise ValueError("API key for Gemini is not set in environment variables")

print(f"API Key: {api_key}")
print(f"API URL: {api_url}")