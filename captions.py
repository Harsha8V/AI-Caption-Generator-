import requests
import streamlit as st

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

def generate_caption(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/chat-bison-001:generateMessage?key={GEMINI_API_KEY}"

    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": {
            "messages": [
                {
                    "author": "user",
                    "content": f"Generate an Instagram caption with trending hashtags for this: {prompt}"
                }
            ]
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "candidates" in result:
            return result["candidates"][0]["content"]
        elif "error" in result:
            st.error(f"🛑 Gemini API error: {result['error'].get('message')}")
        else:
            st.error("🛑 Unexpected response from Gemini.")
        return "⚠️ Failed to generate caption."
    except Exception as e:
        st.error(f"❌ Gemini API call failed: {e}")
        return "⚠️ Failed to generate caption."
