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
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image using Pillow (PIL)
image_path = 'example_01.png'  # Replace with the path to your image
image = Image.open(image_path)

# Get the width and height of the image
width, height = image.size

# Calculate the width and height of each frame
frame_width = width // 9
frame_height = height // 9

# Initialize a list to store the frames
frames = []

# Loop through each row and column to extract frames
for y in range(0, height, frame_height):
    for x in range(0, width, frame_width):
        left = x
        upper = y
        right = x + frame_width
        lower = y + frame_height

        # Crop the image to create a frame
        frame = image.crop((left, upper, right, lower))

        # Convert the image to grayscale (optional, but it simplifies the process) *****
        grayscale_image = image.crop((left, upper, right, lower)).convert('L')

        # Get the width and height of the image
        w, h = grayscale_image.size

        # Check if all pixels are black (0) *****
        is_full_black = all(grayscale_image.getpixel((x, y)) == 0 for x in range(w) for y in range(h))

        if is_full_black:
            print("The image is completely black.")
        else:
            print("The image is not completely black.")
            # Append the frame to the list
            frames.append(frame)

# Save or display the frames as needed
for i, frame in enumerate(frames):
    frame.save(f'frame_{i+1}.png')  # Save each frame as an image file
    # To display the frames, you can use frame.show()

print("Frames created successfully!")

nums = []
numss = []
for i, frame in enumerate(frames):
    # Load the img
    image = cv2.imread(f"frame_{i+1}.png")
    height, width, channels = image.shape

    # Cvt to hsv
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Get binary-mask
    msk = cv2.inRange(hsv, np.array([0, 0, 175]), np.array([179, 255, 255]))
    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=1)
    thr = 255 - cv2.bitwise_and(dlt, msk)

    reduce = 10
    crop_img = thr[reduce:width-reduce, reduce:height-reduce]

    # OCR
    d = pytesseract.image_to_string(crop_img, config="--psm 10")
    if not(d=='_\n' or d=='?\n' or d=='A\n'):
        nums.append(int(d))
    else:
        if (d=='?\n'):
            nums.append(2)
        elif (d=='A\n'):
            nums.append(4)
        else:
            nums.append(0)
    if(len(nums)==9):
        print(nums)
        numss.append(nums)
        nums = []

print(numss)