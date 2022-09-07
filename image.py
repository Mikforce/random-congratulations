#!/usr/bin/env python3
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("1.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

string = pytesseract.image_to_string(image, lang='rus')
print(string)



with open('test1.txt', 'w', encoding='utf-8') as f:
    f.write(str(string))