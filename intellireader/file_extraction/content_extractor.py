import fitz
from pdf2docx import Converter
from response_transition import TextractAnalyzer, LayoutFigureIdentifier, FontSizeEstimator  # Import the new classes
from crop_image_pdf import LayoutFigureGeometry, PDFImagePaster

pdf_path = 'hello2.png'

analyzer = TextractAnalyzer()
textract_response = analyzer.get_response_from_textract(pdf_path)

layout_figure_ids = LayoutFigureIdentifier.find_layout_figure_ids(textract_response['Blocks'])

output_pdf = fitz.open()

# Add a new page to the output PDF with dimensions of a standard US letter size page
page_width, page_height = 595, 842  # Width and height of a standard US letter size page in points
new_page = output_pdf.new_page(width=page_width, height=page_height)

for block in textract_response['Blocks']:
    if block['BlockType'] == 'LINE':  # Check if the block is a line of text
        text = block['Text']  # Extract the text
        geometry_data = block['Geometry']  # Extract the bounding box data
        if block['Id'] not in layout_figure_ids:
            x0 = geometry_data['BoundingBox']['Left'] * page_width
            y0 = geometry_data['BoundingBox']['Top'] * page_height
            # Estimate font size using the FontSizeEstimator class
            font_size = FontSizeEstimator.estimate_font_size(bbox=geometry_data['BoundingBox'])
            # Add the text to the new page at the specified position
            new_page.insert_text((x0, y0), text, fontsize=font_size)  # Use the estimated font size
        else:
            pass

output_pdf_path = 'output_manual_text.pdf'
output_pdf.save(output_pdf_path)
print("New PDF with provided text has been saved.")


geometry_extractor = LayoutFigureGeometry(textract_response)
layout_figures = geometry_extractor.get_layout_figures_geometry()

image_paster = PDFImagePaster(scanned_pdf_path=pdf_path, target_pdf_path=output_pdf_path)
image_paster.paste_cropped_images(layout_figures)

print("Process completed.")

updated_pdf_path = 'updated_' + output_pdf_path
docx_path = "updated_output_manual_text.docx"
cv = Converter(updated_pdf_path)
cv.convert(docx_path)
cv.close()
