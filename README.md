# 📸 AI Instagram Caption Generator (Groq API)

Generate short, catchy Instagram captions with trending hashtags using LLaMA 3 via the Groq API. This project is built with Python and Streamlit and designed for influencers, marketers, and content creators.

## 🚀 Live Demo

https://aicaptiongenerator.streamlit.app/

---

## 🔧 Features

- ✍️ Generate creative, relevant Instagram captions from simple descriptions  
- ⚡ Uses Groq's `llama3-70b-8192` for blazing-fast response  
- 🎨 Clean, styled Streamlit interface with dark/light mode  
- 🔐 API key stored securely via Streamlit Secrets  

---

## 🧱 Tech Stack

| Layer      | Tool                          |
|------------|-------------------------------|
| Backend    | Python 3.9+                    |
| Frontend   | Streamlit                     |
| LLM API    | Groq (LLaMA 3 via OpenAI-compatible endpoint) |
| Styling    | CSS (in `styles/style.css`)   |

---

## 📁 Project Structure

```
groq-caption-generator/
├── app.py                 # Main Streamlit app
├── captions.py            # Groq API logic
├── requirements.txt       # Python dependencies
├── styles/
│   └── style.css          # Custom CSS
└── .streamlit/
    ├── config.toml        # UI theme config
    └── secrets.toml       # Groq API key (not committed)
```

---

## 🧪 Local Development

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/groq-caption-generator.git
cd groq-caption-generator
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create a file at `.streamlit/secrets.toml` with the following content:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📷 Sample Prompt & Output

**Input:**  
> “A rainy coffee shop evening with jazz”

**Output:**  
> “Sippin’ serenity ☕🎷 #RainyVibes #CafeNights #JazzMood”

---

## ☁️ Deployment (Streamlit Cloud)

1. Push to GitHub  
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)  
3. Deploy your repo  
4. Add your Groq key to Secrets as `GROQ_API_KEY`  
5. Done! 🎉

---

## 🧙 Author

Made with ❤️ by **M. Harsha Vardhan**  
📧 harsha.23bce8869@vitapstudent.ac.in  
🔗 [GitHub](https://github.com/Harsha8V)

---

## 📄 License

MIT License
