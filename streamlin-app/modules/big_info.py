# modules/big_info.py

import streamlit as st

def render():
    st.title("📄 BIG-registratie informatie")

    st.markdown("""
    Als buitenlandse tandarts in Nederland moet je je registreren in het BIG-register (Beroepen in de Individuele Gezondheidszorg).

    ### Stappen van het registratieproces:
    1. **Diploma laten erkennen** via DUO of Nuffic
    2. **Bewijs van taalvaardigheid** (Nederlands B2 of C1)
    3. **Kennis- en vaardighedentoets** (BI-toets)
    4. **Aanvraagformulier invullen** bij CIBG
    5. **Beoordeling en registratie**

    👉 Op deze website kun je oefenen voor de BI-toets en je voorbereiden op de Nederlandse tandartspraktijk.
    """)

    st.success("Meer informatie? Bezoek [bigregister.nl](https://www.bigregister.nl)")
