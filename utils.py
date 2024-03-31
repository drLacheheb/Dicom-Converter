import os
import numpy as np
import pydicom
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_images_to_pdf(jpg_filenames, pdf_output_directory="", pdf_filename='output.pdf', page_width=letter[0], page_height=letter[1]):
    """
    Convert a list of JPEG images to a PDF document.

    Args:
        jpg_filenames (list): List of JPEG image filenames.
        pdf_filename (str, optional): Output PDF filename. If None, PDF will not be generated.
        page_width (float): Width of the PDF page.
        page_height (float): Height of the PDF page.
    """

    pdf_path = os.path.join(pdf_output_directory, pdf_filename)
    
    c = canvas.Canvas(pdf_path, pagesize=letter)

    for jpg_filename in jpg_filenames:
        img = Image.open(jpg_filename)
        width_ratio = page_width / img.width
        height = img.height * width_ratio
        os.makedirs(pdf_output_directory, exist_ok=True)
        c.drawImage(jpg_filename, 0, 0, width=page_width, height=height)
        c.showPage()

    if pdf_path:
        c.save()


def get_dcm_filenames(directory):
    """
    Retrieve filenames of DICOM files from a directory.

    Args:
        directory (str): Path to the directory containing DICOM files.

    Returns:
        list: Filenames of DICOM files.
    """
    dcm_filenames = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext.lower() == '.dcm':
                dcm_filenames.append(os.path.join(root, filename))
    return dcm_filenames


def convert_dcm_to_jpg(dcm_filename, output_directory, contrast_factor=1.0, brightness_factor=1.0):
    """
    Convert a DICOM file to a JPEG image.

    Args:
        dcm_filename (str): Filename of the input DICOM file.
        output_directory (str): Directory to save the output JPEG file.
        contrast_factor (float): Factor to adjust contrast.
        brightness_factor (float): Factor to adjust brightness.

    Returns:
        str: Filename of the converted JPEG image.
    """
    dcm_data = pydicom.dcmread(dcm_filename)
    pixel_array = dcm_data.pixel_array.astype(float)

    # Adjust contrast and brightness
    pixel_array = pixel_array * contrast_factor + brightness_factor

    # Normalize pixel values
    pixel_array = np.clip(pixel_array, 0, 255)
    pixel_array = (pixel_array / np.max(pixel_array)) * 255

    # Convert to uint8 and create PIL Image
    image = Image.fromarray(np.uint8(pixel_array))

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Save JPEG file
    jpg_filename = os.path.join(output_directory, os.path.basename(
        dcm_filename).replace('.dcm', '.jpg'))
    image.save(jpg_filename)
    return jpg_filename
