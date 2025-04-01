import streamlit as st

# ВАЖНО: Должно быть первым
st.set_page_config(page_title="Become a Tandarts", page_icon="🦷", layout="wide")

import json
from pathlib import Path
from chapters.block1 import anatomy
from modules import bi_toets

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

query_params = st.query_params
lang = query_params.get("lang", [None])[0]
if lang not in languages:
    lang = st.sidebar.selectbox("🌐 Language", options=list(languages.keys()), format_func=lambda k: languages[k], key="lang")

menu_options = ["🏠 Home", "Syllabus", "BI-Toets", "Flashcards (soon)", "Dutch for Dentists (soon)"]
def_menu = query_params.get("menu", ["🏠 Home"])[0]
if def_menu not in menu_options:
    def_menu = "🏠 Home"
menu = st.sidebar.selectbox("📚 Module:", menu_options, index=menu_options.index(def_menu), key="menu_select")

modules = load_modules()
user_progress = load_progress()

# Интерфейс Syllabus
if menu == "Syllabus":
    st.subheader("📘 Available Modules")
    selected_module = query_params.get("module", [None])[0]

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
                    st.query_params["lang"] = lang
                    st.query_params["menu"] = "Syllabus"
                    st.query_params["module"] = str(module['id'])
                    st.rerun()
        st.markdown("---")

    selected_module = st.query_params.get("module", [None])[0]
    if selected_module:
        selected = next((m for m in modules if m["id"] == selected_module), None)
        if selected:
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
        st.query_params["lang"] = lang
        st.query_params["menu"] = "Syllabus"
        st.query_params["module"] = "block1"
        st.rerun()

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
