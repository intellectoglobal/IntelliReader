from textractor import Textractor
from textractor.data.constants import TextractFeatures


class TextractAnalyzer:
    """
    A class to handle interactions with AWS Textract.
    """
    def __init__(self, region_name="us-east-1"):
        """
        Initializes the TextractAnalyzer with a specific AWS region.
        """
        self.region_name = region_name
        self.extractor = Textractor(region_name=region_name)

    def get_response_from_textract(self, pdf_file_path: str) -> dict:
        """
        Analyzes a document using Textract and returns the response.

        Args:
            pdf_file_path (str): The file path of the PDF document to analyze.

        Returns:
            dict: The response from Textract.
        """
        response = self.extractor.analyze_document(
            file_source=pdf_file_path,
            features=[TextractFeatures.LAYOUT],
            save_image=True
        )
        return response.response

    def get_layout_figures_geometry(self, response: dict) -> list:
        """
        Extracts and returns the geometry data for "LAYOUT_FIGURE" elements.

        Args:
            response (dict): The response from Textract.

        Returns:
            list: A list of geometry data for "LAYOUT_FIGURE" elements.
        """
        layout_figures = []
        for block in response['Blocks']:
            if block['BlockType'] == 'LAYOUT_FIGURE':
                layout_figures.append(block['Geometry']['BoundingBox'])
        return layout_figures


class LayoutFigureIdentifier:
    """
    A class to identify layout figure IDs from Textract response blocks.
    """
    @staticmethod
    def find_layout_figure_ids(blocks):
        """
        Finds and returns the IDs of layout figures in the Textract response blocks.

        Args:
            blocks (list): The blocks from a Textract response.

        Returns:
            list: The IDs of layout figure blocks.
        """
        ids = []
        for block in blocks:
            if block['BlockType'] == 'LAYOUT_FIGURE' and 'Relationships' in block:
                for relationship in block['Relationships']:
                    if relationship['Type'] == 'CHILD':
                        ids.extend(relationship['Ids'])
        return ids


class FontSizeEstimator:
    """
    A class to estimate font size from bounding box dimensions.
    """
    @staticmethod
    def estimate_font_size(bbox, page_height_inches=11):
        """
        Estimates the font size from a bounding box in normalized coordinates.

        Args:
            bbox (dict): A dictionary containing the bounding box with 'Width', 'Height', 'Left', and 'Top' keys.
            page_height_inches (float, optional): The height of the page in inches.

        Returns:
            int: The estimated font size in points.
        """
        bbox_height_inches = bbox['Height'] * page_height_inches
        bbox_height_points = bbox_height_inches * 72
        estimated_padding_points = 2
        estimated_font_size = bbox_height_points - estimated_padding_points

        fractional_part = estimated_font_size % 1
        truncated_font_size = int(estimated_font_size)

        if truncated_font_size % 2 == 1:
            adjusted_font_size = truncated_font_size - 1 + fractional_part
            estimated_font_size = adjusted_font_size

        estimated_font_size = int(round(estimated_font_size))

        if estimated_font_size % 2 == 1:
            estimated_font_size -= 1

        if estimated_font_size < 8:
            return 8
        else:
            return estimated_font_size
