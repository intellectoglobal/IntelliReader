import fitz


class PDFScanner:
    @staticmethod
    def is_scanned(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text("text")
                if not text.strip():
                    return True
            return False
        except Exception as e:
            print(f"Error analyzing PDF: {e}")
            return None


class PDFAnalyzer:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def analyze_pdf(self):
        scanner = PDFScanner()
        result = scanner.is_scanned(self.pdf_path)
        if result is None:
            print("Unable to determine if it's a scanned PDF.")
        elif result:
            print("This is a scanned PDF.")
        else:
            print("This is a normal PDF. Normal PDF is not supported.")
            raise ValueError("Normal PDF is not supported")
