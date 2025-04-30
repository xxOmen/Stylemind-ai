# 👕 StyleMind AI – Outfit Generator (Streamlit + OpenAI DALL·E 3)

StyleMind AI is a Streamlit-powered fashion visualization tool that generates Pinterest-style outfit flat lays using OpenAI's DALL·E 3.

## ✨ Features

- Select options for gender, season, style, and occasion
- Generates 4 visual outfit suggestions using DALL·E 3
- Works with the latest OpenAI SDK (>=1.0.0)
- Deployed securely on Streamlit Cloud with secrets

## 🚀 How to Deploy

### 1. Files You Need

- `stylemind_app_final.py`
- `requirements.txt`

### 2. Add Secret to Streamlit

In your Streamlit Cloud app:
```
OPENAI_API_KEY = "sk-..."
```

### 3. Run Locally (optional)
```bash
pip install -r requirements.txt
streamlit run stylemind_app_final.py
```

## 🧠 Tech Stack

- Streamlit
- OpenAI (DALL·E 3 via `openai.images.generate`)