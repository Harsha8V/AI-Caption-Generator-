import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_caption(prompt):
    response = model.generate_content(
        f"Generate a creative Instagram caption for: {prompt}",
        generation_config={"temperature": 0.9}
    )
    return response.text.strip()
