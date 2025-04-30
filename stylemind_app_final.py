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
    prompt = "Flat lay of a casual summer outfit: white t-shirt, beige chinos, white sneakers, sunglasses. Displayed on a clean beige background."

    image_urls = []
    with st.spinner("Generating 1 outfit image with DALL·E 3..."):
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
        st.success("Here is your outfit suggestion!")
        st.image(image_urls[0], caption="Outfit Suggestion", use_column_width=True)
    else:
        st.warning("No image was generated. Please try again.")
