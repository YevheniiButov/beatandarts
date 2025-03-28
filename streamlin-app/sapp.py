import streamlit as st

st.set_page_config(page_title="Become a Tandarts", page_icon="🦷", layout="wide")

st.title("🦷 Become a Tandarts")
st.write("✅ Streamlit работает! Подключаем модули...")

try:
    from modules import syllabus, bi_toets, flashcards, dutch_phrases, big_info
    from utils.progress import get_all_scores, reset_scores
except Exception as e:
    st.error(f"❌ Ошибка при импорте модулей: {e}")

# ====== Языки ======
languages = {
    "en": "English",
    "nl": "Nederlands",
    "ru": "Русский",
    "es": "Español"
}
lang = st.sidebar.selectbox("🌐 Language / Taal / Язык / Idioma", options=list(languages.keys()), format_func=lambda k: languages[k])

# ====== Главное меню ======
menu = st.sidebar.selectbox("📚 Выберите модуль:", [
    "Syllabus",
    "Dutch for Dentists",
    "Flashcards",
    "BI-Toets",
])

# ====== Контент ======
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

# ====== Прогресс ======
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
