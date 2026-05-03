import streamlit as st

# Seite einrichten
st.set_page_config(page_title="King Kong Grow Systems", page_icon="🦍")
st.title("🦍 King Kong Grow Systems")
st.subheader("Bestellsystem für Partner")

# Partner Auswahl
partner = st.selectbox("Wer bestellt?", ["Greenhope GmbH", "Bavarian Krauts"])

# Box Details
st.markdown("---")
st.markdown("### 📦 Box Details")
groesse = st.selectbox("Größe:", ["Small", "Medium", "Large", "XL"])
design = st.selectbox("Design:", ["Industrial", "Nature", "Black Edition"])
zubehoer = st.multiselect("Zubehör:", ["Aktivkohlefilter", "Bewässerung", "Mess-Kit"])

# Technik-Logik
technik_sets = {
    "Small": "Technik ALPHA (100W)",
    "Medium": "Technik BETA (250W)",
    "Large": "Technik GAMMA (400W)",
    "XL": "Technik DELTA (600W)"
}
technik = technik_sets[groesse]

# Bestell-Button
if st.button("JETZT BESTELLEN"):
    st.success("✅ Bestellung wurde aufgenommen!")
    st.info(f"🔨 Für King Kong: {groesse} Box ({design})")
    st.warning(f"⚡ Für Horti Spectra: Schicke {technik}")
