# modules/syllabus.py

import streamlit as st
from gtts import gTTS
import tempfile
from utils.progress import add_score

# ======== Подключение глав ========
from chapters import ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, ch11, ch12, ch13

chapters = {
    "1 — Wat doet de tandarts?": ch1,
    "2 — Wie werken er in de tandartspraktijk?": ch2,
    "3 — De mond": ch3,
    "4 — De kies": ch4,
    "5 — Mondverzorging / Preventie": ch5,
    "6 — Angst voor de tandarts": ch6,
    "7 — Röntgenfoto’s": ch7,
    "8 — Tandartsbehandelingen": ch8,
    "9 — Aandoeningen in de mond": ch9,
    "10 — Woordenlijst": ch10,
    "11 — De tandartspraktijk": ch11,
    "12 — Hygiëne in de tandartspraktijk": ch12,
    "13 — Communicatie met patiënten": ch13
}

labels = {
    "vocab_title": "📘 Woordenlijst",
    "questions_title": "🧠 Vragen om over na te denken",
    "quiz_title": "🎯 Mini-quiz",
    "submit_answer": "Bevestig je antwoord",
    "correct": "Correct! Goed gedaan.",
    "incorrect": "Helaas, dat is niet correct."
}

def render(lang):
    chapter_select = st.selectbox("📖 Kies een hoofdstuk:", list(chapters.keys()))
    chapter = chapters[chapter_select].get_content()

    st.title(f"🦷 {chapter_select}")
    for p in chapter["paragraphs"]:
        st.write(p)
        if st.button("🔊 " + p[:30] + "...", key=p):
            tts = gTTS(p, lang='nl')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tts.save(tmp.name)
                audio_path = tmp.name
            st.audio(audio_path, format='audio/mp3')

    st.markdown("---")
    st.subheader(labels["vocab_title"])
    for k, v in chapter["vocab"].items():
        st.markdown(f"**{k}** → {v}")

    st.markdown("---")
    st.subheader(labels["questions_title"])
    for q in chapter["questions"]:
        st.markdown(f"- {q}")

    st.markdown("---")
    st.subheader(labels["quiz_title"])
    quiz = chapter["quiz"]
    selected = st.radio(quiz["question"], quiz["options"], key="quiz")
    if st.button(labels["submit_answer"]):
        if selected == quiz["answer"]:
            add_score("syllabus")
            st.success(labels["correct"])
        else:
            st.error(labels["incorrect"])
        st.caption("💡 " + quiz["explanation"])
