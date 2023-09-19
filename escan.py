#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adrian
#
# Created:     17/09/2023
# Copyright:   (c) Adrian 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrimos la imagen
img = cv2.imread("example_01.png")
