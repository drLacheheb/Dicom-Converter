from utils import get_dcm_filenames, convert_dcm_to_jpg, convert_images_to_pdf

# Directory containing DICOM files
input_directory = './input_dicom'
# Output directory for JPEG files
jpeg_output_directory = './output_jpeg'
# Output directory for pdf file
pdf_output_directory = './output_pdf'
# PDF file name
pdf_filename = 'output.pdf'

# Retrieve DICOM filenames
dcm_filenames = get_dcm_filenames(input_directory)

# Convert DICOM to JPEG and save
jpg_filenames = []
for dcm_filename in dcm_filenames:
    jpg_filename = convert_dcm_to_jpg(
        dcm_filename, jpeg_output_directory, contrast_factor=1.5, brightness_factor=50)
    jpg_filenames.append(jpg_filename)

# Convert JPEG images to PDF (optional)
while True:
    convert_to_pdf = input("Do you want to convert JPEG images to PDF? (yes/no): ").lower()
    if convert_to_pdf in ['yes', 'no']:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if convert_to_pdf == 'yes':
    # Prompt the user for PDF filename
    pdf_filename = input("Enter the PDF filename (default: output.pdf): ").strip() or 'output.pdf'

    # Convert JPEG images to PDF
    try:
        convert_images_to_pdf(jpg_filenames, pdf_output_directory, pdf_filename)
        print(f"JPEG images successfully converted to PDF: {os.path.join(pdf_output_directory, pdf_filename)}")
    except Exception as e:
        print(f"Error occurred during PDF conversion: {e}")
else:
    print("JPEG images were not converted to PDF.")