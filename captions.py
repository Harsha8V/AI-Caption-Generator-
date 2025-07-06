import requests
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

def generate_caption(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are an assistant that writes short, catchy Instagram captions with trending hashtags."},
            {"role": "user", "content": f"Generate an Instagram caption for: {prompt}"}
        ],
        "temperature": 0.8
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        st.json(result)  # DEBUG: Show full response

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        elif "error" in result:
            st.error(f"🛑 Groq API error: {result['error']['message']}")
        else:
            st.error("🛑 Unexpected response from Groq.")
        return "⚠️ Failed to generate caption."
    except Exception as e:
        st.error(f"❌ Groq API call failed: {e}")
        return "⚠️ Failed to generate caption."
