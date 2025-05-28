import streamlit as st
from PIL import Image
import easyocr
import language_tool_python
import tempfile

st.title("Õpilastöö automaatne kontroll (EasyOCR versioon)")

# OCR-i laadimine ainult üks kord
@st.cache_resource
def load_reader():
    st.info("Laen OCR mudelit... See võib võtta hetke ⏳")
    return easyocr.Reader(['et'], gpu=False)

reader = load_reader()

uploaded_file = st.file_uploader("Lae üles pilt (JPG või PNG)", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Laetud töö", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        image.save(tmp_file.name)
        tmp_path = tmp_file.name

    st.subheader("Tuvastatud tekst:")
    results = reader.readtext(tmp_path, detail=0)
    extracted_text = "\n".join(results)
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
