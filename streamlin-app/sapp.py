import streamlit as st
import urllib.parse

# Настройка страницы
st.set_page_config(page_title="Become a Tandarts", page_icon="🦷", layout="wide")

# Стилизация и логотип
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom, #f7f2ec, #e2eaf1) !important;
        font-family: 'Open Sans', sans-serif !important;
        color: #2a2a2a !important;
    }
    .stApp {
        background: linear-gradient(to bottom, #f7f2ec, #e2eaf1) !important;
    }
    .stButton>button {
        background-color: #7c8b9f !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #5d6d7c !important;
    }
    h1, h2, h3 {
        color: #2f3e46 !important;
    }
    </style>

    <div style="text-align: center; margin-top: -2rem; margin-bottom: 2rem;">
        <img src="/static/favicon.png" alt="logo" style="height: 60px;" />
        <h1 style="margin-bottom: 0; font-weight: 300; font-size: 2.2rem;">Become a Tandarts</h1>
        <p style="color: #555; margin-top: 0.5rem;">Platform for foreign dentists in the Netherlands</p>
        <hr style="border: none; height: 1px; background: #ccc; margin: 2rem auto 1rem;" />
    </div>
""", unsafe_allow_html=True)

# Языки
languages = {
    "en": "English",
    "nl": "Nederlands",
    "ru": "Русский",
    "uk": "Українська",
    "es": "Español",
    "tr": "Türkçe",
    "fa": "فارسی",
    "pt": "Português"
}

# Получение языка из URL или выбор из списка
query_params = st.experimental_get_query_params()
lang = query_params.get("lang", [None])[0]
if lang not in languages:
    lang = st.sidebar.selectbox("🌐 Language / Taal / Язык / Idioma", options=list(languages.keys()), format_func=lambda k: languages[k])

# Главное меню
menu = st.sidebar.selectbox("📚 Module:", [
    "Syllabus",
    "BI-Toets",
    "Flashcards (soon)",
    "Dutch for Dentists (soon)"
])

# Импорты модулей
try:
    from chapters.block1 import anatomy
    # from chapters.block2 import orthodontie
    # from chapters.block3 import endodontie
    from modules import bi_toets
    # from modules import flashcards, dutch_phrases
except Exception as e:
    st.error(f"❌ Ошибка при импорте модулей: {e}")

# Рендеринг по выбору
try:
    if menu == "Syllabus":
        anatomy.show(lang)
    elif menu == "BI-Toets":
        bi_toets.render(lang)
    elif menu == "Flashcards (soon)":
        st.info("📌 Flashcards module coming soon.")
    elif menu == "Dutch for Dentists (soon)":
        st.info("📌 Dutch practice module coming soon.")
except Exception as e:
    st.error(f"❌ Ошибка в модуле '{menu}': {e}")
