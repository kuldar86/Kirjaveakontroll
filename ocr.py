import easyocr
import tempfile

reader = easyocr.Reader(['et'], gpu=False)

def extract_text_from_image(image):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        image.save(tmp_file.name)
        results = reader.readtext(tmp_file.name, detail=0)
    return "\n".join(results)
