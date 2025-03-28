# utils/progress.py

import streamlit as st

# Используем сессионное состояние для хранения баллов
if "scores" not in st.session_state:
    st.session_state.scores = {}

def add_score(module_name):
    st.session_state.scores[module_name] = st.session_state.scores.get(module_name, 0) + 1

def get_all_scores():
    return st.session_state.get("scores", {})

def reset_scores():
    st.session_state.scores = {}
