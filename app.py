import streamlit as st
from captions import generate_caption
from utils import get_hashtags

st.markdown("<style>" + open('styles/style.css').read() + "</style>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1>📱 AI Instagram Caption Assistant</h1>
        <p style='color:gray;'>Describe your post and get catchy captions with trending hashtags ✨</p>
    </div>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Insta Caption Wizard", page_icon="📸")
st.title("📱 AI Instagram Caption Assistant")

description = st.text_input("Describe your post (e.g., 'sunset by the beach')")

category = st.selectbox("Choose a category", ["travel", "food", "fashion", "tech", "fitness"])

if st.button("Generate Caption"):
    with st.spinner("Summoning captions..."):
        caption = generate_caption(description)
        hashtags = " ".join(get_hashtags(category))
        full_caption = f"{caption}\n\n{hashtags}"
        st.text_area("✨ Your Caption", value=full_caption, height=150)
        st.success("Caption ready! You can copy and use it 🚀")

