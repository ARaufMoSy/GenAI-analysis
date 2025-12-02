import os
import google.generativeai as genai

# Try GEMINI_API_KEY first, fall back to GOOGLE_API_KEY
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("No API key found. Set GEMINI_API_KEY or GOOGLE_API_KEY in your environment.")

# Configure the SDK
genai.configure(api_key=api_key)

# Use the Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

# Generate content
response = model.generate_content("Hello, explain tokens in 2 sentences")
print(response.text)
