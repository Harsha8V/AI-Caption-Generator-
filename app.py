import streamlit as st
from captions import generate_caption

st.set_page_config(page_title="📸 AI Caption Generator", layout="centered")

# Optional: CSS
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

st.title("📸 AI Instagram Caption Generator")
st.markdown("Enter a photo description below, and the AI will generate a creative caption with hashtags.")

description = st.text_input("Describe your Instagram post 👇")

if st.button("✨ Generate Caption"):
    if description.strip():
        caption = generate_caption(description)
        if caption:
            st.success("📝 Here's your AI-generated caption:")
            st.code(caption, language="markdown")
        else:
            st.error("❌ Failed to generate caption.")
    else:
        st.warning("Please enter a description.")
