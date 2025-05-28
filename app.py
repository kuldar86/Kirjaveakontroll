import streamlit as st
from PIL import Image
from ocr import extract_text_from_image
from spellcheck import check_spelling

st.title("Kirjaveakontroll õpilastöödele")

uploaded_file = st.file_uploader("Lae üles pilt (.jpg või .png)", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Laetud töö", use_container_width=True)

    with st.spinner("Tuvastan teksti..."):
        text = extract_text_from_image(image)
        st.subheader("Tuvastatud tekst:")
        st.write(text)

    with st.spinner("Kontrollin kirjavigu..."):
        errors = check_spelling(text)
        st.subheader("Leitud kirjavead:")
        if errors:
            for e in errors:
                st.markdown(f"- **{e['context']}** → _{e['message']}_ (soovitus: {e['replacements']})")
        else:
            st.success("Kirjavigu ei tuvastatud!")
