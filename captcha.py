try:
        from PIL import Image
except ImportError:
        import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
captcha = pytesseract.image_to_string(Image.open('ce.jpg'),config='-psm 8 -c tessedit_char_whitelist=0123456789')
captcha = captcha.replace(" ", "").strip()
print(captcha)
print(captcha)
