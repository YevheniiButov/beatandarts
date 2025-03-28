import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Become a Tandarts", page_icon="🦷", layout="wide")

# Кастомный стиль и логотип
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

# Импорты с отладкой
try:
    from modules import syllabus, bi_toets, flashcards, dutch_phrases, big_info
    from utils.progress import get_all_scores, reset_scores
except Exception as e:
    st.error(f"❌ Ошибка при импорте модулей: {e}")

# Выбор языка
languages = {
    "en": "English",
    "nl": "Nederlands",
    "ru": "Русский",
    "es": "Español"
}
lang = st.sidebar.selectbox("🌐 Language / Taal / Язык / Idioma", options=list(languages.keys()), format_func=lambda k: languages[k])

# Главное меню
menu = st.sidebar.selectbox("📚 Kies een module:", [
    "Syllabus",
    "Dutch for Dentists",
    "Flashcards",
    "BI-Toets",
])

# Отображение выбранного модуля
try:
    if menu == "Syllabus":
        syllabus.render(lang)
    elif menu == "Dutch for Dentists":
        dutch_phrases.render(lang)
    elif menu == "Flashcards":
        flashcards.render(lang)
    elif menu == "BI-Toets":
        bi_toets.render(lang)
except Exception as e:
    st.error(f"❌ Ошибка при отображении модуля '{menu}': {e}")

# Прогресс и сброс
try:
    with st.sidebar.expander("📈 Progress"):
        scores = get_all_scores()
        for k, v in scores.items():
            st.write(f"**{k}**: {v} баллов")

        if st.button("🔁 Reset scores"):
            reset_scores()
            st.success("Scores have been reset.")
except Exception as e:
    st.error(f"❌ Ошибка в блоке прогресса: {e}")
