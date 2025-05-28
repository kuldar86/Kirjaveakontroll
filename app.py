import streamlit as st
from PIL import Image
import pytesseract
import language_tool_python

st.title("Õpilastöö automaatne kontroll")

uploaded_file = st.file_uploader("Lae üles pilt (JPG või PNG)", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Laetud töö", use_column_width=True)

    st.subheader("Tuvastatud tekst:")
    extracted_text = pytesseract.image_to_string(image, lang='est')
    st.write(extracted_text)

    st.subheader("Leitud kirjavead:")
    tool = language_tool_python.LanguageTool('et')
    matches = tool.check(extracted_text)

    if matches:
        for match in matches:
            st.markdown(f"- **{match.context}**")
            st.markdown(f"  ↪ {match.message} (_Soovitus: {match.replacements}_)")
    else:
        st.success("Kirjavigu ei tuvastatud! 👍")
