import requests
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

def generate_caption(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [{"text": f"Generate an Instagram caption with relevant hashtags for: {prompt}"}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        st.error(f"❌ Gemini API error: {e}")
        return "⚠️ Failed to generate caption."
