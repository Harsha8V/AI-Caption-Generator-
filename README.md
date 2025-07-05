
# 📸 AI Instagram Caption Generator

Create engaging, creative Instagram captions with trending hashtags using Google’s Gemini Pro model. Perfect for influencers, marketers, and content creators who want fresh caption ideas instantly.

![Screenshot](https://user-images.githubusercontent.com/placeholder/screenshot.png) <!-- Replace this with your actual screenshot -->

---

## 🚀 Live Demo

🟢 [Try the App on Streamlit Cloud](https://your-streamlit-cloud-link.streamlit.app)

---

## 🧠 Features

- Generate AI-powered captions using **Gemini Pro (MakerSuite API)**
- Trending hashtags automatically included
- Clean, responsive Streamlit web app
- Copy-to-clipboard caption support
- Easily customizable categories (future support)

---

## 🛠️ Tech Stack

| Layer        | Tools                        |
|--------------|------------------------------|
| Frontend UI  | Streamlit + HTML/CSS         |
| AI Engine    | Gemini Pro (via REST API)    |
| Language     | Python 3                     |
| Hosting      | Streamlit Cloud              |

---

## 📁 Project Structure

```
ai-caption-generator/
├── app.py                # Main web app (Streamlit)
├── captions.py           # Gemini API logic
├── styles/
│   └── style.css         # Custom styling
├── requirements.txt      # Python dependencies
└── .streamlit/
    └── config.toml       # Streamlit deployment config
```

---

## 🔐 Environment Secrets (Streamlit Cloud)

Go to the **Secrets tab** and add:

```toml
GEMINI_API_KEY = "AIzaSyAE5DFwvti72wigTfJGXt8a55OLpeH9JfU"
```

Get your API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 🖥️ Local Development

1. Clone the repo:

```bash
git clone https://github.com/your-username/ai-caption-generator.git
cd ai-caption-generator
```

2. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Run the app locally:

```bash
streamlit run app.py
```

5. (Optional) Create a `.streamlit/secrets.toml` for local dev:

```toml
GEMINI_API_KEY = "your-makersuite-api-key"
```

---

## ✨ Example Input & Output

**Input:**  
> A photo of a dog with sunglasses on the beach

**Output:**  
> "Living that paw-some beach life 🐾🌴☀️ #SandyPaws #BeachVibes #DogDays #CoolCanine"

---

## 📦 Deployment (Streamlit Cloud)

1. Push your project to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo and deploy
4. Add your API key in **Secrets**
5. Done!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✍️ Author

Developed by **M. Harsha Vardhan**  
VIT AP University – CSE (AI/ML)  
📧 harsha.23bce8869@vitapstudent.ac.in  
🔗 [GitHub](https://github.com/Harsha8V)
