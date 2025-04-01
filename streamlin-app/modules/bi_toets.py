import streamlit as st
from utils.progress import add_score

# === Вопросы ===
questions = [
    {
        "question": "Wat is de aanbevolen manier om instrumenten te steriliseren?",
        "options": ["In water met zeep", "Met alcohol", "Met een autoclaaf"],
        "answer": "Met een autoclaaf",
        "explanation": "Een autoclaaf doodt bacteriën, virussen en schimmels onder hoge druk en temperatuur."
    },
    {
        "question": "Wat hoort bij goede handhygiëne?",
        "options": ["Handschoenen hergebruiken", "Sieraden dragen", "Handen wassen voor en na contact"],
        "answer": "Handen wassen voor en na contact",
        "explanation": "Handen wassen voorkomt verspreiding van infecties."
    },
    {
        "question": "Wat betekent informed consent?",
        "options": ["De patiënt beslist na uitleg", "De arts beslist", "De verzekering beslist"],
        "answer": "De patiënt beslist na uitleg",
        "explanation": "De patiënt moet weten wat er gaat gebeuren en akkoord gaan."
    },
    {
        "question": "Wat is een mogelijk gevolg van onvoldoende sterilisatie?",
        "options": ["Verlies van instrumenten", "Verspreiding van infecties", "Geen effect"],
        "answer": "Verspreiding van infecties",
        "explanation": "Onvoldoende sterilisatie verhoogt het risico op kruisbesmetting."
    },
    {
        "question": "Wat is de functie van een medisch dossier?",
        "options": ["Voor administratie", "Voor onderzoek", "Voor communicatie en continuïteit van zorg"],
        "answer": "Voor communicatie en continuïteit van zorg",
        "explanation": "Een dossier helpt zorgverleners samen te werken en het verloop te volgen."
    }
]

# === Инициализация состояния ===
if "bi_q_index" not in st.session_state:
    st.session_state.bi_q_index = 0
    st.session_state.bi_score = 0
    st.session_state.bi_confirmed = False
    st.session_state.bi_done = False

# === Отображение ===
def render(lang):
    st.title("🧪 BI-toets voorbereiding")

    if "bi_done" not in st.session_state:
    st.session_state.bi_done = False
if "bi_q_index" not in st.session_state:
    st.session_state.bi_q_index = 0
if "bi_score" not in st.session_state:
    st.session_state.bi_score = 0
if "bi_confirmed" not in st.session_state:
    st.session_state.bi_confirmed = False


    if st.session_state.bi_done:
        st.success(f"Je hebt {st.session_state.bi_score} van {len(questions)} goed beantwoord!")
        if st.button("🔁 Opnieuw beginnen"):
            st.session_state.bi_q_index = 0
            st.session_state.bi_score = 0
            st.session_state.bi_confirmed = False
            st.session_state.bi_done = False
            st.rerun()
        return

    q = questions[st.session_state.bi_q_index]
    st.markdown(f"### Vraag {st.session_state.bi_q_index + 1} van {len(questions)}")
    st.write(f"**{q['question']}**")

    if f"selected_{st.session_state.bi_q_index}" not in st.session_state:
        st.session_state[f"selected_{st.session_state.bi_q_index}"] = None

    if not st.session_state.bi_confirmed:
        st.session_state[f"selected_{st.session_state.bi_q_index}"] = st.radio(
            "Kies het juiste antwoord:",
            q['options'],
            key=f"q_{st.session_state.bi_q_index}"
        )

        if st.button("Bevestigen"):
            if st.session_state[f"selected_{st.session_state.bi_q_index}"] == q['answer']:
                st.success("✅ Correct!")
                st.session_state.bi_score += 1
                add_score("bi_toets")
            else:
                st.error("❌ Onjuist.")
            st.info(f"ℹ️ {q['explanation']}")
            st.session_state.bi_confirmed = True
            st.rerun()
    else:
        st.markdown(f"**Je antwoord:** {st.session_state[f'selected_{st.session_state.bi_q_index}']}")
        if st.session_state[f"selected_{st.session_state.bi_q_index}"] == q['answer']:
            st.success("✅ Correct!")
        else:
            st.error("❌ Onjuist.")
        st.info(f"ℹ️ {q['explanation']}")

        if st.session_state.bi_q_index + 1 < len(questions):
            if st.button("Volgende vraag"):
                st.session_state.bi_q_index += 1
                st.session_state.bi_confirmed = False
                st.rerun()
        else:
            if st.button("Bekijk resultaat"):
                st.session_state.bi_done = True
                st.rerun()
