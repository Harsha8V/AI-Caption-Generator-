import google.generativeai as genai
import streamlit as st

# Use Gemini MakerSuite API key securely
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load the Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

def generate_caption(prompt):
    try:
        response = model.generate_content(
            f"Generate an engaging Instagram caption for this: {prompt}",
            generation_config={"temperature": 0.9}
        )
        return response.text.strip()
    except Exception as e:
        st.error(f"❌ Gemini API error: {e}")
        return "⚠️ Error generating caption."
