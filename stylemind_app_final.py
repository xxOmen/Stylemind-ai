# Streamlit App for StyleMind AI: Clean & Compatible with OpenAI SDK ≥ 1.0.0

import streamlit as st
import openai

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="StyleMind AI", layout="centered")
st.title("👕 StyleMind AI – Outfit Generator with Images")
st.write("Generate stylish outfit visuals using OpenAI DALL·E 3.")

# --- User Input Form ---
with st.form("style_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"])
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"])
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"])
    submitted = st.form_submit_button("Generate Outfit Images")

if submitted:
    prompt = f"A flat lay of a {style.lower()} outfit for a {gender.lower()} attending a {occasion.lower()} in {season.lower()}. Include top, bottom, shoes, and 1–2 accessories on a clean background."

    image_urls = []
    with st.spinner("Generating 4 outfit images with DALL·E 3..."):
        for _ in range(4):
            try:
                response = openai.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1
                )
                image_urls.append(response.data[0].url)
            except Exception as e:
                st.error(f"Error generating image: {e}")

    if image_urls:
        st.success("Here are your outfit suggestions!")
        cols = st.columns(2)
        for i, url in enumerate(image_urls):
            with cols[i % 2]:
                st.image(url, caption=f"Outfit Suggestion {i+1}", use_column_width=True)
    else:
        st.warning("No images were generated. Please try again.")
