import fitz
import os
# The PdfMerger class is used to merge multiple PDF files into a single PDF file.
class PdfMerger:
    @staticmethod
    def merge_pdfs(input_files, output_folder, output_file):
        """
        Merge multiple PDF files into a single PDF.

        :param input_files: List of input PDF file paths to merge.
        :param output_folder: Path of the output folder for the merged PDF.
        :param output_file: Name of the output PDF file.
        """
        pdf_merger = fitz.open()

        for input_file in input_files:
            pdf = fitz.open(input_file)
            pdf_merger.insert_pdf(pdf)

        output_path = os.path.join(output_folder, output_file)
        
        output_pdf = fitz.open()  # Create a new PDF document for the merged result
        output_pdf.insert_pdf(pdf_merger)  # Insert the merged content into the new document
        
        output_pdf.save(output_path)
        output_pdf.close()

    @staticmethod
    def get_user_input(message, is_path=False, default=None):
        """
        Get user input with optional default value.

        :param message: Message to display to the user.
        :param is_path: True if the input should be treated as a file path.
        :param default: Default value for the input.
        :return: User input or the default value if provided.
        """
        while True:
            user_input = input(f"{message} ({default}): ").strip() if default else input(f"{message}: ").strip()

            # If a default value is provided and the user entered nothing, use the default
            if default and not user_input:
                return default

            # If the input should be treated as a path and it's not an absolute path, make it absolute
            if is_path and not os.path.isabs(user_input):
                user_input = os.path.abspath(user_input)

            return user_input