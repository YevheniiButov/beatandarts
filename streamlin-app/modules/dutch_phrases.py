# modules/dutch_phrases.py

import streamlit as st
from utils.progress import add_score
import random

phrases = [
    {"nl": "Open je mond alsjeblieft", "en": "Please open your mouth"},
    {"nl": "Bijt niet", "en": "Don’t bite"},
    {"nl": "Iets meer open", "en": "Open a bit more"},
    {"nl": "Niet bewegen", "en": "Don’t move"},
    {"nl": "Gaat het?", "en": "Are you okay?"},
    {"nl": "Slik eens", "en": "Please swallow"},
]

def render(lang):
    st.title("💬 Dutch for Dentists")

    phrase = random.choice(phrases)
    st.header(f"🦷 {phrase['nl']}")
    if st.button("Vertaling tonen"):
        st.info(f"💡 {phrase['en']}")
        add_score("dutch")
