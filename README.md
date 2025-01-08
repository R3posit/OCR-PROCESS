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

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/OCR-PROCESS.git
   cd OCR-PROCESS
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set the Tesseract executable path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   ```

---

## Usage
1. Run the script:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Use your mouse to position the cursor and press `Enter` to select the top-left and bottom-right corners of the area you want to capture.
   - The program will automatically process the selected area, extract text using OCR, and save it to `Sorular_NotDefteri.txt`.

3. Repeat the process for new areas or stop the program by pressing `Ctrl+C`.

---

## File Structure
- `main.py`: The main script containing the functionality.
- `requirements.txt`: List of required Python packages.
- `Sorular_NotDefteri.txt`: The output file where extracted text is saved.

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

