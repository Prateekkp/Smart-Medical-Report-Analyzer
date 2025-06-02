# PDG - OCR Extraction and PDF Processing

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import fitz

# ✅ PDF se direct text nikaalne ke liye
def extract_text_from_pdf(path):
    doc = fitz.open(path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text.strip()

# ✅ Image (JPG/PNG) se text OCR karke nikaalne ke liye
def extract_text_from_image(path):
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    return text.strip()