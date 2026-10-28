
import streamlit as st
import asyncio
from googletrans import Translator, LANGUAGES
st.set_page_config(page_title="Language Decoder", page_icon="🌍")
st.title("🌍 Smart Language Detector")
st.write("Welcome to the Smart Language Detector!")
st.write("Enter a sentence in any language to detect its language.")
st.divider()
st.header("Detect a Language")
sentence = st.text_area("Enter your sentence:")
async def detect_language(text):
    async with Translator() as translator:
        result = await translator.translate(text, src="auto", dest="en")
        return result.src
if st.button("Detect Language"):
    if sentence.strip():
        try:
            language_code = asyncio.run(detect_language(sentence))
            language = LANGUAGES.get(language_code, language_code)
            st.success(f"Detected Language: {language.title()}")
            st.write(f"Language Code: {language_code}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a sentence.")
