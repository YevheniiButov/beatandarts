import streamlit as st
import json
import os

def load_translation(lang):
    file_path = os.path.join("translations", f"{lang}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"❌ Translation file error: {e}")
        return {}

def show(lang="en"):
    t = load_translation(lang)

    # 🔍 Покажем, что именно загружается
    st.write("📥 LOADED TRANSLATION:", t)

    if not t:
        st.warning("⚠️ Could not load translation.")
        return

    st.title(t.get("block1.title", "🧐 Block 1.1: Anatomy and Physiology of the Masticatory System"))

    st.markdown("""
### 🔍 {chewing_header}
- **{chewing_0}**
- **{chewing_1}**
- **{chewing_2}**
- **{chewing_3}**

- **{swallowing_0}**
- **{swallowing_1}**
- **{swallowing_2}**

- **{structures}**

- **Nerves:**
  - {nerve_v}
  - {nerve_vii}
  - {nerve_ix}
  - {nerve_x}

---

### 💪 {innervation_header}
- {sensory}
- {motor}
- {vessels}
- {landmarks}

---

### 🏙️ {tmj_header}
- {tmj_anatomy}
- {tmj_movements}
- {tmj_assessment}
- {tmj_pathology}
    """.format(
        chewing_header=t.get("block1.chewing.header", "Physiology of Chewing and Swallowing"),
        chewing_0=t.get("block1.chewing.phases", ["..."])[0],
        chewing_1=t.get("block1.chewing.phases", ["", "..."])[1],
        chewing_2=t.get("block1.chewing.phases", ["", "", "..."])[2],
        chewing_3=t.get("block1.chewing.phases", ["", "", "", "..."])[3],
        swallowing_0=t.get("block1.swallowing.phases", ["..."])[0],
        swallowing_1=t.get("block1.swallowing.phases", ["", "..."])[1],
        swallowing_2=t.get("block1.swallowing.phases", ["", "", "..."])[2],
        structures=t.get("block1.chewing.structures", "Tongue, soft palate, epiglottis, pharyngeal muscles"),
        nerve_v=t.get("block1.chewing.nerves", {}).get("V", "n. trigeminus — mastication"),
        nerve_vii=t.get("block1.chewing.nerves", {}).get("VII", "n. facialis — facial expression"),
        nerve_ix=t.get("block1.chewing.nerves", {}).get("IX", "n. glossopharyngeus — sensation and swallowing"),
        nerve_x=t.get("block1.chewing.nerves", {}).get("X", "n. vagus — swallowing and epiglottis"),
        innervation_header=t.get("block1.innervation.header", "Innervation and Blood Supply"),
        sensory=t.get("block1.innervation.sensory", "Sensory innervation of the jaws"),
        motor=t.get("block1.innervation.motor", "Motor innervation: m. masseter, temporalis, pterygoideus"),
        vessels=t.get("block1.innervation.vessels", "Blood supply: a. maxillaris and a. alveolaris inferior"),
        landmarks=t.get("block1.innervation.landmarks", "Landmarks: infraorbital, mental, mandibular foramina"),
        tmj_header=t.get("block1.tmj.header", "Temporomandibular Joint (TMJ)"),
        tmj_anatomy=t.get("block1.tmj.anatomy", "Anatomy: head, fossa, disc, capsule, ligaments"),
        tmj_movements=t.get("block1.tmj.movements", "Movements: rotation, translation, combination"),
        tmj_assessment=t.get("block1.tmj.assessment", "Clinical: opening, deviation, palpation"),
        tmj_pathology=t.get("block1.tmj.pathology", "TMD: pain, limitation, dislocation")
    ))