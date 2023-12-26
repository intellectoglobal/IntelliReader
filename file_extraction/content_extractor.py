import fitz
from pdf2docx import Converter
from response_transition import TextractAnalyzer, LayoutFigureIdentifier, FontSizeEstimator  # Import the new classes

pdf_path = 'hello.pdf'

# Initialize the TextractAnalyzer and get the Textract response
analyzer = TextractAnalyzer()
textract_response = analyzer.get_response_from_textract(pdf_path)

# Find layout figure IDs using the LayoutFigureIdentifier class
layout_figure_ids = LayoutFigureIdentifier.find_layout_figure_ids(textract_response['Blocks'])

# Create a new PDF document for the output
output_pdf = fitz.open()  # Create a new, empty PDF document

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

# Save the new PDF with the provided text
output_pdf_path = 'output_manual_text.pdf'
output_pdf.save(output_pdf_path)
print("New PDF with provided text has been saved.")

# Convert the new PDF to a Word document using pdf2docx
docx_path = "output_pdftodocx_file.docx"  # Define the path for the output DOCX file
cv = Converter(output_pdf_path)  # Initialize the converter with the path to the new PDF
cv.convert(docx_path)  # Convert the PDF to DOCX
cv.close()  # Close the converter

print("PDF has been converted to DOCX and saved.")
