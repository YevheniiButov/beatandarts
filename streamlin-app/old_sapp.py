import streamlit as st
st.set_page_config(page_title="Become a Tandarts", page_icon="🦷", layout="wide")

import urllib.parse
import json
from pathlib import Path


# Загрузка модулей, прогресса и сохранение результатов

def load_modules():
    modules_path = Path("data/modules.json")
    if modules_path.exists():
        with open(modules_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def load_progress():
    progress_path = Path("data/progress.json")
    if progress_path.exists():
        with open(progress_path, "r", encoding="utf-8") as f:
            return json.load(f).get("progress", {})
    return {}

def save_progress(module_id: str, score: int):
    path = Path("data/progress.json")
    data = {"user_id": "demo_user", "progress": {}}
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            try:
    if menu == "🏠 Home":
        # Home content
        st.markdown("""
            <div style="text-align: center; margin-top: -2rem; margin-bottom: 2rem;">
                <img src="/static/favicon.png" alt="logo" style="height: 60px;" />
                <h1 style="margin-bottom: 0; font-weight: 300; font-size: 2.2rem;">Become a Tandarts</h1>
                <p style="color: #555; margin-top: 0.5rem;">Platform for foreign dentists in the Netherlands</p>
                <hr style="border: none; height: 1px; background: #ccc; margin: 2rem auto 1rem;" />
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {translations['start_title'][lang]}")
        if st.button(translations["start_button"][lang]):
            st.query_params = {"lang": lang, "menu": "Syllabus", "module": "block1"}
            st.rerun()

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(translations["card_1_title"][lang])
            st.write(translations["card_1_desc"][lang])
        with col2:
            st.subheader(translations["card_2_title"][lang])
            st.write(translations["card_2_desc"][lang])
        with col3:
            st.subheader(translations["card_3_title"][lang])
            st.write(translations["card_3_desc"][lang])

    elif menu == "Syllabus":
        if selected_module is None:
            st.query_params = {"lang": lang, "menu": "Syllabus", "module": "block1"}
            st.rerun()

        elif selected_module == "block1":
            anatomy.show(lang)
            st.markdown("---")
            st.subheader("🧪 Mini Test")

            q1 = st.radio("1. Which nerve innervates the masseter muscle?", ["n. facialis (VII)", "n. trigeminus (V)", "n. glossopharyngeus (IX)"], index=0)
            q2 = st.radio("2. What is the role of the TMJ?", ["To digest food", "To perform mastication movements", "To swallow"], index=0)
            q3 = st.radio("3. Where is the foramen mentale located?", ["In the maxilla", "In the mandible", "In the zygomatic bone"], index=0)

            if st.button("📊 Submit Answers"):
                score = 0
                if q1 == "n. trigeminus (V)": score += 1
                if q2 == "To perform mastication movements": score += 1
                if q3 == "In the mandible": score += 1

                percent = round((score / 3) * 100)
                save_progress("block1", percent)
                st.success(f"✅ You scored {percent}%! Progress saved. You can now access the next module.")

        elif selected_module == "block2":
            st.header("🧲 Block 2: Orthodontics")
            st.markdown("""
            In this block, we explore the fundamentals of orthodontics: brackets, retainers, and biomechanics of tooth movement.
            
            ### 🦷 Topics:
            - Fixed appliances
            - Clear aligners
            - Retention phase
            - Tooth movement physiology
            
            ---
            
            ### 🧪 Mini Test
            """)

            q1 = st.radio("1. What is the main purpose of a retainer?", ["Move teeth", "Maintain position", "Whiten teeth"], index=0)
            q2 = st.radio("2. Which appliance is often invisible?", ["Brackets", "Aligners", "Bands"], index=0)
            q3 = st.radio("3. What type of force moves teeth?", ["Compressive", "Light continuous", "Electrical"], index=0)

            if st.button("📊 Submit Answers", key="b2quiz"):
                score = 0
                if q1 == "Maintain position": score += 1
                if q2 == "Aligners": score += 1
                if q3 == "Light continuous": score += 1

                percent = round((score / 3) * 100)
                save_progress("block2", percent)
                st.success(f"✅ You scored {percent}%! Progress saved. You can now access the next module.")

        elif selected_module == "block3":
            st.header("🦷 Block 3: Endodontics")
            st.markdown("""
            This block covers root canal anatomy, instruments, and treatment techniques.

            ### 📌 Topics:
            - Root canal system
            - Access cavity preparation
            - Working length determination
            - Cleaning and shaping
            - Obturation

            ---

            ### 🧪 Mini Test
            """)

            q1 = st.radio("1. What is the purpose of working length determination?", ["To choose the right filling", "To know canal length", "To clean the tooth surface"], index=0)
            q2 = st.radio("2. Which instrument is used to clean canals?", ["Curette", "Endo file", "Explorer"], index=0)
            q3 = st.radio("3. What is gutta-percha used for?", ["Irrigation", "Filling canals", "Making crowns"], index=0)

            if st.button("📊 Submit Answers", key="b3quiz"):
                score = 0
                if q1 == "To know canal length": score += 1
                if q2 == "Endo file": score += 1
                if q3 == "Filling canals": score += 1

                percent = round((score / 3) * 100)
                save_progress("block3", percent)
                st.success(f"✅ You scored {percent}%! Progress saved. You can now access the next module.")

        else:
            st.subheader("📘 Available Modules")
            for module in modules:
                title = module["title"].get(lang, module["title"].get("en"))
                desc = module["description"].get(lang, module["description"].get("en"))
                prerequisite = module.get("prerequisite")
                if prerequisite:
                    required_id = prerequisite.get("module_id")
                    user_score = user_progress.get(required_id, 0)
                else:
                    user_score = 100

                locked = False
                if prerequisite:
                    required_id = prerequisite.get("module_id")
                    min_score = prerequisite.get("min_score", 0)
                    locked = user_score < min_score

                with st.container():
                    st.markdown(f"### {title}")
                    st.markdown(f"📝 {desc}")
                    if locked:
                        st.warning("🔒 Locked — complete the previous module to unlock.")
                    else:
                        if st.button(f"Open {title}", key=module["id"]):
                            st.query_params = {"lang": lang, "menu": "Syllabus", "module": module["id"]}
                            st.rerun()
                    st.markdown("---")

    elif menu == "BI-Toets":
        bi_toets.render(lang)

    elif menu == "Flashcards (soon)":
        st.info("📌 Flashcards module coming soon.")

    elif menu == "Dutch for Dentists (soon)":
        st.info("📌 Dutch practice module coming soon.")

except Exception as e:
    st.error(f"❌ Ошибка при импорте модулей: {e}")

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
""", unsafe_allow_html=True)

# Отображение контента
try:
    selected_module = query_params.get("module", [None])[0]

    if menu == "🏠 Home":
        # (оставляем Home как есть)
        pass

    elif menu == "Syllabus":
        if selected_module is None:
            st.query_params = {"lang": lang, "menu": "Syllabus", "module": "block1"}
            st.rerun()

        elif selected_module == "block1":
            anatomy.show(lang)
            st.markdown("---")
            st.subheader("🧪 Mini Test")
            # ... (тест по block1)

        elif selected_module == "block2":
            # ... (block2 + тест)
            pass

        elif selected_module == "block3":
            # ... (block3 + тест)
            pass

        else:
            st.subheader("📘 Available Modules")
            # ... (список блоков)

    elif menu == "BI-Toets":
        bi_toets.render(lang)
    elif menu == "Flashcards (soon)":
        st.info("📌 Flashcards module coming soon.")
    elif menu == "Dutch for Dentists (soon)":
        st.info("📌 Dutch practice module coming soon.")
except Exception as e:
    st.error(f"❌ Ошибка в модуле '{menu}': {e}")
