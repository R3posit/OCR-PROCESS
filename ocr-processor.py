import pyautogui
from PIL import ImageGrab, Image
import os
from datetime import datetime
import pytesseract
import keyboard
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def wait_for_enter():
    print("Devam etmek için 'Enter' tuşuna basın.")
    while True:
        if keyboard.is_pressed("enter"):
            time.sleep(0.5)
            break

def select_area():
    print("İlk noktayı seçmek için mouse imlecini konumlandırın ve 'Enter'a basın.")
    wait_for_enter()
    x1, y1 = pyautogui.position()
    print(f"İlk nokta seçildi: ({x1}, {y1})")

    print("İkinci noktayı seçmek için mouse imlecini konumlandırın ve 'Enter'a basın.")
    wait_for_enter()
    x2, y2 = pyautogui.position()
    print(f"İkinci nokta seçildi: ({x2}, {y2})")

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    return (x1, y1, x2, y2)

def capture_screenshot(area):
    x1, y1, x2, y2 = area
    try:
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        print("Ekran görüntüsü başarıyla alındı.")
        temp_file = "temp_screenshot.png"
        screenshot.save(temp_file, "PNG")
        loaded_image = Image.open(temp_file)
        return loaded_image
    except Exception as e:
        print(f"Ekran görüntüsü alınırken hata oluştu: {e}")
        return None

def extract_text_from_image(image):
    try:
        image = image.convert("RGB")
        extracted_text = pytesseract.image_to_string(image, lang="tur")
        return extracted_text
    except Exception as e:
        print(f"OCR işlemi sırasında hata oluştu: {e}")
        return ""

def save_to_notebook(question):
    filename = "Sorular_NotDefteri.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"\nSoru Alındı: {timestamp}\n")
            file.write(f"Soru:\n{question}\n")
            file.write("-" * 40 + "\n")
        print("Metin başarıyla kaydedildi.")
    except Exception as e:
        print(f"Metin kaydedilirken hata oluştu: {e}")

def main():
    print("Program başlatılıyor...")
    while True:
        area = select_area()
        screenshot = capture_screenshot(area)

        if screenshot is not None:
            print("OCR ile metin çıkarılıyor...")
            image_text = extract_text_from_image(screenshot)

            print("Metin not defterine kaydediliyor...")
            save_to_notebook(image_text)

        print("Yeni bir alan seçmek için işlemi tekrarlayın veya programı durdurmak için 'Ctrl+C'ye basın.")

if __name__ == "__main__":
    main()
