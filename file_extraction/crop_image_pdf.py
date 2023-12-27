import fitz  # PyMuPDF


class LayoutFigureGeometry:
    def __init__(self, response: dict):
        self.response = response

    def get_layout_figures_geometry(self) -> list:
        layout_figures = []
        for block in self.response['Blocks']:
            if block['BlockType'] == 'LAYOUT_FIGURE':
                layout_figures.append(block['Geometry']['BoundingBox'])
        return layout_figures


class PDFImagePaster:
    def __init__(self, scanned_pdf_path: str, target_pdf_path: str):
        self.scanned_pdf_path = scanned_pdf_path
        self.target_pdf_path = target_pdf_path

    def paste_cropped_images(self, layout_figures):
        scanned_pdf = fitz.open(self.scanned_pdf_path)
        target_pdf = fitz.open(self.target_pdf_path)

        if len(target_pdf) == 0:
            target_pdf.new_page(width=scanned_pdf[0].rect.width, height=scanned_pdf[0].rect.height)

        scanned_page = scanned_pdf[0]
        target_page = target_pdf[0]

        for figure in layout_figures:
            x0 = figure['Left'] * scanned_page.rect.width
            y0 = figure['Top'] * scanned_page.rect.height
            x1 = x0 + figure['Width'] * scanned_page.rect.width
            y1 = y0 + figure['Height'] * scanned_page.rect.height
            crop_rect = fitz.Rect(x0, y0, x1, y1)

            clip = scanned_page.get_pixmap(clip=crop_rect)
            target_page.insert_image(crop_rect, pixmap=clip)

        new_target_pdf_path = 'updated_' + self.target_pdf_path
        target_pdf.save(new_target_pdf_path)
        print("Updated PDF has been saved to:", new_target_pdf_path)