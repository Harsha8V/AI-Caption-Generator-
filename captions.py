import requests
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

def generate_caption(user_input):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/text-bison-001:generateText?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "prompt": {
            "text": f"Write a short, catchy Instagram caption with trending hashtags for the following post: {user_input}"
        },
        "temperature": 0.7,
        "candidateCount": 1
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "candidates" in result:
            return result["candidates"][0]["output"]
        elif "error" in result:
            st.error(f"🛑 Gemini API error: {result['error'].get('message')}")
        else:
            st.error("🛑 Unexpected response from Gemini.")
        return "⚠️ Failed to generate caption."
    except Exception as e:
        st.error(f"❌ Gemini API call failed: {e}")
        return "⚠️ Failed to generate caption."
