import streamlit as st
import urllib.parse

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

# Переводы для главной страницы
translations = {
    "start_title": {
        "en": "Start your BIG journey",
        "ru": "Начни путь к BIG-регистрации",
        "nl": "Begin je BIG-reis",
        "uk": "Почни свій шлях до BIG",
        "es": "Comienza tu camino BIG",
        "tr": "BIG yolculuğuna başla",
        "fa": "سفر BIG خود را آغاز کنید",
        "pt": "Comece sua jornada BIG"
    },
    "start_button": {
        "en": "🚀 Start Learning",
        "ru": "🚀 Начать обучение",
        "nl": "🚀 Start met leren",
        "uk": "🚀 Почати навчання",
        "es": "🚀 Comenzar a estudiar",
        "tr": "🚀 Öğrenmeye başla",
        "fa": "🚀 شروع یادگیری",
        "pt": "🚀 Começar a aprender"
    },
    "card_1_title": {
        "en": "📚 About the Platform",
        "ru": "📚 О платформе",
        "nl": "📚 Over het platform",
        "uk": "📚 Про платформу",
        "es": "📚 Sobre la plataforma",
        "tr": "📚 Platform hakkında",
        "fa": "📚 درباره پلتفرم",
        "pt": "📚 Sobre a plataforma"
    },
    "card_1_desc": {
        "en": "Online preparation for BIG registration in the Netherlands for dentists trained abroad.",
        "ru": "Онлайн-подготовка к BIG-регистрации в Нидерландах для стоматологов из других стран.",
        "nl": "Online voorbereiding op BIG-registratie in Nederland voor tandartsen uit het buitenland.",
        "uk": "Онлайн-підготовка до BIG-регістрації в Нідерландах для стоматологів з інших країн.",
        "es": "Preparación online para el registro BIG en los Países Bajos para dentistas extranjeros.",
        "tr": "Hollanda'da BIG kaydı için yurtdışında eğitim görmüş diş hekimlerine online hazırlık.",
        "fa": "آمادگی آنلاین برای ثبت‌نام BIG در هلند برای دندانپزشکان آموزش دیده در خارج.",
        "pt": "Preparação online para o registro BIG nos Países Baixos para dentistas formados no exterior."
    },
    "card_2_title": {
        "en": "📝 Tests & Simulations",
        "ru": "📝 Тесты и симуляции",
        "nl": "📝 Toetsen en simulaties",
        "uk": "📝 Тести та симуляції",
        "es": "📝 Pruebas y simulaciones",
        "tr": "📝 Testler ve simülasyonlar",
        "fa": "📝 آزمون‌ها و شبیه‌سازی‌ها",
        "pt": "📝 Testes e Simulações"
    },
    "card_2_desc": {
        "en": "Practice BI-toets and other real exam simulations online in one place.",
        "ru": "Тренируйся с BI-toets и другими экзаменами онлайн в одном месте.",
        "nl": "Oefen BI-toets en andere echte examenvragen online op één plek.",
        "uk": "Практика BI-toets та інших реальних іспитів онлайн.",
        "es": "Practica BI-toets y otros exámenes reales en línea en un solo lugar.",
        "tr": "BI-toets ve diğer gerçek sınav simülasyonlarını çevrimiçi olarak çalış.",
        "fa": "تمرین BI-toets و شبیه‌سازی امتحانات واقعی در یک مکان.",
        "pt": "Pratique BI-toets e outros exames reais online em um só lugar."
    },
    "card_3_title": {
        "en": "📖 Learning Materials",
        "ru": "📖 Учебные материалы",
        "nl": "📖 Leermateriaal",
        "uk": "📖 Навчальні матеріали",
        "es": "📖 Materiales de aprendizaje",
        "tr": "📖 Öğrenme materyalleri",
        "fa": "📖 مواد آموزشی",
        "pt": "📖 Materiais de Aprendizagem"
    },
    "card_3_desc": {
        "en": "Guides, books, syllabi and step-by-step instructions for the full registration procedure.",
        "ru": "Руководства, книги, учебные планы и пошаговые инструкции для полной регистрации.",
        "nl": "Gidsen, boeken, syllabi en stapsgewijze instructies voor de volledige registratieprocedure.",
        "uk": "Посібники, книги, програми та покрокові інструкції для повної реєстрації.",
        "es": "Guías, libros, programas e instrucciones paso a paso para todo el registro.",
        "tr": "Kılavuzlar, kitaplar, ders planları ve adım adım kayıt talimatları.",
        "fa": "راهنماها، کتاب‌ها، برنامه‌های درسی و دستورالعمل‌های گام به گام برای ثبت کامل.",
        "pt": "Guias, livros, programas e instruções passo a passo para o registro completo."
    }
}

# Получение языка из URL или выбор из списка
query_params = st.query_params
lang = query_params.get("lang", [None])[0]
if lang not in languages:
    lang = st.sidebar.selectbox("🌐 Language / Taal / Язык / Idioma", options=list(languages.keys()), format_func=lambda k: languages[k])

# Главное меню
menu = st.sidebar.selectbox("📚 Module:", [
    "🏠 Home",
    "Syllabus",
    "BI-Toets",
    "Flashcards (soon)",
    "Dutch for Dentists (soon)"
])

# Импорты модулей
try:
    from chapters.block1 import anatomy
    from modules import bi_toets
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
    if selected_module == "block1":
        anatomy.show(lang)
    # Здесь можно добавить аналогично block2, block3 и т.д.
    if menu == "🏠 Home":
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
            st.query_params = {"lang": lang}
            st.session_state["menu"] = "Syllabus"
            st.experimental_rerun()

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
        st.subheader("📘 Available Modules")
        for module in modules:
            title = module["title"].get(lang, module["title"].get("en"))
            desc = module["description"].get(lang, module["description"].get("en"))
            prerequisite = module.get("prerequisite")
            user_score = 100  # 💡 здесь позже будет реальный прогресс из файла

            locked = False
            if prerequisite:
                required_id = prerequisite.get("module_id")
                min_score = prerequisite.get("min_score", 0)
                # пока временно: если prerequisite есть — блокируем
                # (в будущем здесь проверим user_score из progress.json)
                locked = True  # ← временно блокируем все, кроме block1

            with st.container():
                st.markdown(f"### {title}")
                st.markdown(f"📝 {desc}")
                if locked:
                    st.warning("🔒 Locked — complete the previous module to unlock.")
                else:
                    if st.button(f"Open {title}", key=module["id"]):
                        st.query_params = {"lang": lang, "module": module["id"]}
                        st.experimental_rerun()
                st.markdown("---")
    elif menu == "BI-Toets":
        bi_toets.render(lang)
    elif menu == "Flashcards (soon)":
        st.info("📌 Flashcards module coming soon.")
    elif menu == "Dutch for Dentists (soon)":
        st.info("📌 Dutch practice module coming soon.")
except Exception as e:
    st.error(f"❌ Ошибка в модуле '{menu}': {e}")
