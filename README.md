# DICOM Converter

Converts DICOM to image and PDF document , with optional settings for contrast and brightness adjustment.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview
This script converts DICOM images to PDF documents using Python. It leverages the PyDicom library to read DICOM files, and the Pillow and ReportLab libraries for image processing and PDF generation, respectively.

## Features
- Converts DICOM images to JPEG format with optional contrast and brightness adjustment.
- Supports conversion of JPEG images to PDF documents.
- Provides flexibility for customizing PDF output settings.

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your_username/dicom-converter.git
```

2. Navigate to the project directory:

```bash
cd dicom-to-pdf
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
1. Place your DICOM files in the `input_directory` folder.
2. Run the script:

```bash
python main.py
```

3. Follow the prompts to convert DICOM images to PDF.

## Customization
- **Input Directory**: Change the directory containing DICOM files by modifying the `input_directory` variable in `main.py`.
- **Output Directory for JPEG Files**: Customize the output directory for JPEG files by adjusting the `jpeg_output_directory` variable in `main.py`.
- **Output Directory for PDF File**: Modify the output directory for the PDF file by changing the `pdf_output_directory` variable in `main.py`.
- **PDF File Name**: Adjust the name of the PDF file by modifying the `pdf_filename` variable in `main.py`.

## Dependencies
- [PyDicom](https://github.com/pydicom/pydicom): for reading DICOM files.
- [Pillow](https://github.com/python-pillow/Pillow): for image processing.
- [ReportLab](https://bitbucket.org/rptlab/reportlab/src/default/): for PDF generation.
- [NumPy](https://github.com/numpy/numpy): for numerical operations.

## Contributing
Contributions are welcome!.

## License
just give me a star in github and use it as you like