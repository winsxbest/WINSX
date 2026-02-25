import streamlit as st
import datetime

# Saýtyň ady
st.set_page_config(page_title="Meniň Python Günlügim")

st.title("📱 Gündelik Python Kodlarym")

# Kodlary saklajak faýlymyz
DB_FILE = "mening_kodlarym.txt"

# --- TÄZE KOD GOŞMAK BÖLÜMI ---
with st.sidebar:
    st.header("➕ Täze Kod Goş")
    bashlyk = st.text_input("Mowzugyň ady:")
    taze_kod = st.text_area("Python kodyňyzy şu ýere ýazyň:ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpkNHBpekRickhwSFRIR2tXanlwUmM4@144.124.247.137:30380#WINSX%20%0A%D0%9D%D0%B8%D0%B4%D0%B5%D1%80%D0%BB%D0%B0%D0%BD%D0%B4%D1%8B%F0%9F%87%B3%F0%9F%87%B1", height=150)
    
    if st.button("Saýta goş"):
        if bashlyk and taze_kod:
            wagty = datetime.datetime.now().strftime("%d.%m.%Y")
            with open(DB_FILE, "a", encoding="utf-8") as f:
                # Maglumatlaryň arasyny ýörite belgiler bilen bölýäris
                f.write(f"DATE:{wagty}|TITLE:{bashlyk}|CODE:{taze_kod}END_KOD\n")
            st.success("Kod üstünlikli goşuldy!")
        else:
            st.error("Gözlegleri dolduryň!")

# --- KODLARY GÖRKEZMEK BÖLÜMI ---
try:
    with open(DB_FILE, "r", encoding="utf-8") as f:
        data = f.readlines()
        
    for setir in reversed(data): # Iň täze kod iň ýokarda bolsun
        if "END_KOD" in setir:
            # Maglumaty bölmek
            wagty = setir.split("DATE:")[1].split("|TITLE:")[0]
            bashlyk = setir.split("TITLE:")[1].split("|CODE:")[0]
            kody = setir.split("CODE:")[1].split("END_KOD")[0]
            
            with st.container():
                st.markdown(f"### 📅 {wagty} - {bashlyk}")
                st.code(kody, language='python')
                st.divider()
except FileNotFoundError:
    st.info("Heniz hiç hili kod goýulmady. Çep menýudan ilkinji koduňyzy goşuň!")
