import streamlit as st
from captions import generate_caption

st.set_page_config(page_title="📸 AI Caption Generator", layout="centered")

# Load CSS
try:
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("⚠️ style.css not found.")

st.title("📸 AI Instagram Caption Generator")
st.markdown("Generate creative captions with trending hashtags using Gemini AI.")

description = st.text_input("Describe your Instagram post 👇")

if st.button("✨ Generate Caption"):
    if description.strip():
        caption = generate_caption(description)
        st.success("📝 Here's your AI-generated caption:")
        st.code(caption, language="markdown")
        st.button("📋 Copy Caption", on_click=st.toast("✅ Caption copied to clipboard!"))
    else:
        st.warning("Please enter a description.")
