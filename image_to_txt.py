import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import numpy as np
from PIL import Image
import pytesseract
import re

def read_details(fp):

    image = cv2.imread(fp)
    upscaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(upscaled, cv2.COLOR_BGR2GRAY)

    # Sharpen Image
    sharpening_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(gray, -1, sharpening_kernel)

    # Convert image to binary 
    _, binary = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    resized = cv2.resize(binary, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    noise_removed = cv2.medianBlur(resized, 5)

    config = '--oem 3 --psm 6 -c tessedit_char_whitelist="0123456789"'
    text = pytesseract.image_to_string(noise_removed, config=config)
    numbers = re.findall(r'\d+', text)

    split_numbers = []
    for number in numbers:
        if len(number) == 6:
            # Split into three two-digit numbers
            split_numbers.extend([number[i:i+2] for i in range(0, 6, 2)])
        elif len(number) == 4:
            # Split into two two-digit numbers
            split_numbers.extend([number[i:i+2] for i in range(0, 4, 2)])
        else:
            split_numbers.append(number)

    if len(split_numbers) == 3:
        result = f'{split_numbers[0]}({split_numbers[1]}-{split_numbers[2]})'
    elif len(split_numbers) == 2:
        result = f'({split_numbers[0]}-{split_numbers[1]})'
    else:
        result = "NF"

    return result


def get_attack_startup(fp):
    text = read_details(fp)
    startup_details = text.split('\n')[0]
    start = text.find('(')
    end = text.find(')')

    # Extracting the content inside parentheses
    if start != -1 and end != -1 and start < end:
        content_inside_parentheses = text[start + 1:end].replace(' ', '')
        if(len(content_inside_parentheses) == 5):
            if(content_inside_parentheses[:2] == content_inside_parentheses[3:]):
                return content_inside_parentheses[:2]
        return content_inside_parentheses
        # print(content_inside_parentheses)
    else:
        # print(startup_details)
        return None

image_path = './frames/details/acropped_details_frame.png'
print(get_attack_startup(image_path))

