import streamlit as st
from PIL import Image
import pytesseract

def extract_text(image):
    return pytesseract.image_to_string(image, lang='est')

st.set_page_config(page_title="Kirjaveakontroll", layout="centered")
st.title("Kirjaveakontroll – v0.0.1")

uploaded_file = st.file_uploader("Lae üles käsikirjaline etteütlus (.jpg/.png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Laetud pilt", use_column_width=True)

    with st.spinner("Tuvastan teksti..."):
        text = extract_text(image)

    st.subheader("Tuvastatud tekst (OCR):")
    st.text_area("OCR tulemus", text, height=200)

    # Näidisparandus
    if "koolii" in text:
        st.markdown("**Parandusettepanek:** `koolii → kooli`")
    else:
        st.markdown("_Parandusi ei tuvastatud selles demoversioonis._")