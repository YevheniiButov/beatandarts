# Become a Tandarts

An online platform to help foreign-trained dentists prepare for BIG-registration in the Netherlands 🇳🇱🦷

---

## 🔧 Project Structure

- `sapp.py`: main Streamlit app
- `/modules/modules.json`: structure of educational blocks (multilingual)
- `/chapters/`: contains code for each learning block (e.g., `block1`, `block2`, etc.)
- `/static/`: contains logo, favicon, etc.

---

## ✅ Features

- Streamlit-based UI with multilingual support (EN, RU, NL, etc.)
- Dynamic loading of modules from `modules.json`
- Modular structure: each block is a learning unit with prerequisites
- Beautiful UI adapted from Flask front-end

---

## 🚀 Getting Started

```bash
uvicorn main:app --reload   # если ты используешь FastAPI в Flask части
streamlit run sapp.py       # запуск Streamlit-приложения
