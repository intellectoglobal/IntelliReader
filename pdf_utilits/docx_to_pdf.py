# import subprocess
import subprocess
class Docx2PdfConverter:
    def __init__(self, input_path):
        self.word_file = input_path

    def convert_docx_to_pdf_linux(self):
        """
        Converts the input DOCX file to a PDF file.

        Returns:
        - bool: True if the conversion is successful, False otherwise.
        """
        try:
            subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", self.word_file, "--outdir", "out_folder"])
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")
            return False


input_file = "sample4.docx"
converter = Docx2PdfConverter(input_file)
converter.convert_docx_to_pdf_linux()