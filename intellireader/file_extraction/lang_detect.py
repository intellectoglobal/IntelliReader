import pytesseract
from langdetect import detect
from pdf2image import convert_from_path


class PDFConverter:
    @staticmethod
    def convert_to_images(pdf_path):
        images = []
        try:
            pages = convert_from_path(pdf_path)
            for i, page in enumerate(pages):
                image_path = f"{pdf_path}_page_{i + 1}.png"
                page.save(image_path, 'PNG')
                images.append(image_path)
            return images
        except Exception as e:
            print(f"Error converting PDF to images: {e}")
            return None


class LanguageDetector:
    def __init__(self):
        self.supported_languages = [
            'en', 'de', 'fr', 'es', 'it', 'pt', 'tel', 'hin', 'tam', 'eng', 'mal', 'kan', 'ben', 'mar', 'san'
        ]

    def detect_from_image(self, image_path):
        try:
            text = pytesseract.image_to_string(image_path, lang='+'.join(self.supported_languages))
            detected_lang = detect(text)
            print(f"Detected language is {detected_lang}")
            return detected_lang
        except Exception as e:
            print(f"Error detecting language from image: {e}")
            return None
