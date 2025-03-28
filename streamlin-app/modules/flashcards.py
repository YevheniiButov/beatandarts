# modules/flashcards.py

import streamlit as st
import random
from utils.progress import add_score

# 🔤 Пример слов для тренировки
words = {
    "tandarts": "dentist",
    "wortelkanaal": "root canal",
    "kies": "molar",
    "tandvlees": "gum",
    "röntgenfoto": "X-ray",
    "verdoving": "anesthesia"
}

def render(lang):
    st.title("🧠 Flashcards voor Tandartsen")
    word = random.choice(list(words.keys()))
    
    st.write("👉 Wat betekent het woord:")
    st.header(f"📘 {word}")

    if st.button("Toon vertaling"):
        st.success(f"✅ {words[word]}")
        add_score("flashcards")
