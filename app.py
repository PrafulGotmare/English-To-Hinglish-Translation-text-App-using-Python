import streamlit as st
from mtranslate import translate

def translate_to_hinglish(text):
    hinglish_translation = translate(text, to_language='hi', from_language='en')
    return hinglish_translation

def main():
    st.title("English to Hinglish Translation App")
    
    input_text = st.text_area("Enter English text:")
    if st.button("Translate"):
        hinglish_translation = translate_to_hinglish(input_text)
        st.success(f"Hinglish Translation: {hinglish_translation}")

if __name__ == "__main__":
    main()

