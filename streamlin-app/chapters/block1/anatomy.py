import streamlit as st
import json
import os

def load_translation(lang):
    file_path = os.path.join("translations", f"{lang}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def show(lang="en"):
    t = load_translation(lang)

    st.title(t.get("block1.title", "🧐 Block 1.1: Anatomie en fysiologie van het kauwstelsel"))

    st.markdown(f"""
### 🔍 {t.get('block1.chewing.header', 'Физиология жевания и глотания')}
- **{t.get('block1.chewing.phases', ['Фазы жевания:'])[0]}**
- **{t.get('block1.chewing.phases', [''])[1]}**
- **{t.get('block1.chewing.phases', [''])[2]}**
- **{t.get('block1.chewing.phases', [''])[3]}**

- **{t.get('block1.swallowing.phases', ['Фазы глотания:'])[0]}**
- **{t.get('block1.swallowing.phases', [''])[1]}**
- **{t.get('block1.swallowing.phases', [''])[2]}**

- **{t.get('block1.chewing.structures', 'Участвуют структуры: язык, мягкое нёбо, надгортанник, мышцы глотки')}**

- **Нервы:**
  - {t.get('block1.chewing.nerves', {}).get('V', '*n. trigeminus (V)* — жевательные мышцы')}
  - {t.get('block1.chewing.nerves', {}).get('VII', '*n. facialis (VII)* — мимика, контроль губ')}
  - {t.get('block1.chewing.nerves', {}).get('IX', '*n. glossopharyngeus (IX)* — сенсорика и начало глотания')}
  - {t.get('block1.chewing.nerves', {}).get('X', '*n. vagus (X)* — глотание, надгортанник')}

---

### 💪 {t.get('block1.innervation.header', 'Иннервация и кровоснабжение')}
- {t.get('block1.innervation.sensory', 'Чувствительная иннервация верхней и нижней челюсти')}
- {t.get('block1.innervation.motor', 'Моторная иннервация: m. masseter, temporalis, pterygoideus')}
- {t.get('block1.innervation.vessels', 'Кровоснабжение: a. maxillaris и a. alveolaris inferior')}
- {t.get('block1.innervation.landmarks', 'Ориентиры: foramen infraorbitale, mentale, mandibulae')}

---

### 🏙️ {t.get('block1.tmj.header', 'ВНЧС (temporomandibulair gewricht)')}
- {t.get('block1.tmj.anatomy', 'Анатомия: головка, суставная ямка, диск, капсула, связки')}
- {t.get('block1.tmj.movements', 'Движения: ротация, трансляция, комбинированные')}
- {t.get('block1.tmj.assessment', 'Клиническая оценка: открытие рта, отклонение, пальпация')}
- {t.get('block1.tmj.pathology', 'Патологии: TMD, боль, ограничение, вывих')}
    """)
