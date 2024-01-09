import fitz
from pdf2docx import Converter
from response_transition import TextractAnalyzer, LayoutFigureIdentifier, FontSizeEstimator
from crop_image_pdf import LayoutFigureGeometry, PDFImagePaster
from lang_detect import LanguageDetector, PDFConverter
import os
from pdf_analyze import PDFAnalyzer


def get_textract_response(pdf_path):
    analyzer = TextractAnalyzer()
    return analyzer.get_response_from_textract(pdf_path)


def create_output_pdf(textract_response, page_width=595, page_height=842):
    output_pdf = fitz.open()
    new_page = output_pdf.new_page(width=page_width, height=page_height)

    layout_figure_ids = LayoutFigureIdentifier.find_layout_figure_ids(textract_response['Blocks'])

    for block in textract_response['Blocks']:
        if block['BlockType'] == 'LINE':
            text = block['Text']
            geometry_data = block['Geometry']
            if block['Id'] not in layout_figure_ids:
                x0 = geometry_data['BoundingBox']['Left'] * page_width
                y0 = geometry_data['BoundingBox']['Top'] * page_height
                font_size = FontSizeEstimator.estimate_font_size(bbox=geometry_data['BoundingBox'])
                new_page.insert_text((x0, y0), text, fontsize=font_size)

    return output_pdf


def paste_images_to_pdf(pdf_path, output_pdf, textract_response):
    geometry_extractor = LayoutFigureGeometry(textract_response)
    layout_figures = geometry_extractor.get_layout_figures_geometry()

    image_paster = PDFImagePaster(scanned_pdf_path=pdf_path, target_pdf_path=output_pdf_path)
    image_paster.paste_cropped_images(layout_figures)


def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()


class MainScript:
    def __init__(self):
        self.lang_detector = LanguageDetector()

    def process_input(self, input_path, output_pdf_path, updated_pdf_path, docx_path):
        analyzer = PDFAnalyzer(input_path)
        try:
            analyzer.analyze_pdf()
        except ValueError as e:
            print(f"Error: {e}")
            return
        if input_path.lower().endswith('.pdf'):
            images = PDFConverter.convert_to_images(input_path)
            if images:
                detected_languages = []
                for img in images:
                    detected_lang = self.lang_detector.detect_from_image(img)
                    detected_languages.append(detected_lang)
                    os.remove(img)

                # Assuming all pages should have the same language for simplicity
                detected_language = detected_languages[0] if detected_languages else None
        else:
            detected_language = self.lang_detector.detect_from_image(input_path)

        print(f"Detected language is {detected_language}")
        supported_languages = ['en', 'de', 'fr', 'es', 'it', 'pt']

        if detected_language not in supported_languages:
            print(f"This file's language '{detected_language}' is not supported.")
            return

        textract_response = get_textract_response(pdf_path)
        output_pdf = create_output_pdf(textract_response)
        output_pdf.save(output_pdf_path)
        print("New PDF with provided text has been saved.")

        paste_images_to_pdf(pdf_path, output_pdf_path, textract_response)
        print("Process completed.")

        convert_pdf_to_docx(updated_pdf_path, docx_path)


if __name__ == "__main__":
    pdf_path = 'hello2.png'
    output_pdf_path = 'output_manual_text.pdf'
    updated_pdf_path = 'updated_' + output_pdf_path
    docx_path = "updated_output_manual_text.docx"

    main_script = MainScript()
    main_script.process_input(pdf_path, output_pdf_path, updated_pdf_path, docx_path)
