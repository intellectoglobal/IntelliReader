# Importing necessary modules
from pdf2docx import Converter


class Pdf2DocxConverter:
    """
    A class for converting PDF files to DOCX format.

    Attributes:
    - input_path (str): The path to the input PDF file.
    - output_path (str): The path to save the output DOCX file.

    Methods:
    - convert_pdf_to_docx(): Converts the input PDF file to a DOCX file.
    """
    def __init__(self, input_path, output_path):
        """
        Initializes a Pdf2DocxConverter object.

        Parameters:
        - input_path (str): The path to the input PDF file.
        - output_path (str): The path to save the output DOCX file.
        """
        self.input_path = input_path
        self.output_path = output_path

    def convert_pdf_to_docx(self):
        """
        Converts the input PDF file to a DOCX file.
        Returns:
        - None
        """
        cv = Converter(self.input_path)
        cv.convert(self.output_path)
        cv.close()