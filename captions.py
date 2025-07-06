import requests
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

def generate_caption(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Write a short, engaging Instagram caption with trending hashtags for this description: {prompt}"
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        elif "error" in result:
            st.error(f"🛑 Gemini API error: {result['error'].get('message')}")
        else:
            st.error("🛑 Unexpected response from Gemini.")
        return "⚠️ Failed to generate caption."
    except Exception as e:
        st.error(f"❌ Gemini API call failed: {e}")
        return "⚠️ Failed to generate caption."
