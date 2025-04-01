import streamlit as st
import json
from pathlib import Path
from chapters.block1 import anatomy
from modules import bi_toets

# ВАЖНО: Должно быть первым
st.set_page_config(page_title="Become a Tandarts", page_icon="🦷", layout="wide")

# Загрузка данных
def load_modules():
    path = Path("streamlin-app/data/modules.json")
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def load_progress():
    path = Path("data/progress.json")
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f).get("progress", {})
    return {}

def save_progress(module_id: str, score: int):
    path = Path("data/progress.json")
    data = {"user_id": "demo_user", "progress": {}}
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                pass
    if "progress" not in data:
        data["progress"] = {}
    data["progress"][module_id] = max(score, data["progress"].get(module_id, 0))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

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

if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang = st.sidebar.selectbox("🌐 Language", options=list(languages.keys()), format_func=lambda k: languages[k], index=list(languages.keys()).index(st.session_state.lang))
st.session_state.lang = lang

menu_options = ["🏠 Home", "Syllabus", "BI-Toets", "Flashcards (soon)", "Dutch for Dentists (soon)"]
menu = st.sidebar.selectbox("📚 Module:", menu_options, key="menu_select")

modules = load_modules()
user_progress = load_progress()

# Интерфейс Syllabus
if menu == "Syllabus":
    st.subheader("📘 Available Modules")

    for module in modules:
        title = module["title"].get(lang, module["title"].get("en"))
        desc = module["description"].get(lang, module["description"].get("en"))

        prerequisite = module.get("prerequisite")
        if prerequisite:
            required_id = prerequisite.get("module_id")
            user_score = user_progress.get(required_id, 0)
            min_score = prerequisite.get("min_score", 0)
            locked = user_score < min_score
        else:
            locked = False

        with st.container():
            st.markdown(f"### {title}")
            st.markdown(f"📝 {desc}")

            if locked:
                st.warning("🔒 Locked — complete the previous module to unlock.")
            else:
                btn_key = f"open_{module['id']}"
                if st.button(f"Open {title}", key=btn_key):
                    st.session_state.selected_module = module["id"]
            st.markdown("---")

    selected_module = st.session_state.get("selected_module")
    if selected_module:
        selected = next((m for m in modules if m["id"] == selected_module), None)
        if selected:
            st.markdown(f"## ✅ You opened: {selected['title'].get(lang, '...')}")
            if selected["id"] == "block1":
                anatomy.show(lang)
            elif selected["id"] == "block2":
                st.header("🧲 Block 2: Orthodontics")
                st.write("Coming soon...")
            elif selected["id"] == "block3":
                st.header("🦷 Block 3: Endodontics")
                st.write("Coming soon...")

elif menu == "🏠 Home":
    st.title("Become a Tandarts")
    st.write("Platform for foreign dentists in the Netherlands")
    if st.button("🚀 Start Learning"):
        st.session_state.selected_module = "block1"

elif menu == "BI-Toets":
    if "bi_done" not in st.session_state:
        st.session_state.bi_done = False
        st.session_state.bi_q_index = 0
        st.session_state.bi_score = 0

    bi_toets.render(lang)

elif menu == "Flashcards (soon)":
    st.info("📌 Flashcards module coming soon.")

elif menu == "Dutch for Dentists (soon)":
    st.info("📌 Dutch practice module coming soon.")