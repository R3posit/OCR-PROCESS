# OCR-PROCESS

## Overview
**OCR-PROCESS** is a Python-based application that enables users to capture a selected area of their screen, extract text from the captured image using Optical Character Recognition (OCR), and save the extracted text to a notebook file with timestamps. The tool is designed to be user-friendly and versatile, supporting tasks like digital note-taking, document processing, and more.

---

## Features
- **Interactive Area Selection**: Allows users to define a specific screen area using their mouse.
- **Screenshot Capture**: Captures the selected screen area as an image.
- **OCR Text Extraction**: Processes the image using Tesseract OCR to extract text (supports Turkish and other languages).
- **Organized Text Storage**: Saves extracted text with timestamps into a structured TXT file for future reference.
- **Error Handling**: Handles potential errors during the screenshot and OCR processes to ensure reliability.

---

## Prerequisites
Before running the project, ensure the following dependencies are installed:

- **Python 3.x**
- **Pillow**: For image handling
- **PyAutoGUI**: For mouse and screen automation
- **pytesseract**: For OCR functionality
- **Keyboard**: For detecting key presses

Additionally, you must have Tesseract OCR installed on your system. Download it from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

---

## Notes
- Ensure the selected screen area contains clear and legible text for accurate OCR results.
- For non-Turkish text, modify the OCR language in the script by changing the `lang` parameter (e.g., `lang="eng"` for English).

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.

