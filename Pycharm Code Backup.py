# Import required packages
import cv2
# import pytesseract

# Mention the installed location of Tesseract-OCR in your system
# pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'

# Read image from which text needs to be extracted
img = cv2.imread("part1.jpeg")

# Preprocessing the image starts

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
print(len(contours))
# Creating a copy of image
im2 = img.copy()

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]


new_contours = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio_1 = h / w
    aspect_ratio_2 = w / h
    if aspect_ratio_1 < 3 and aspect_ratio_2 < 2 and w > 12 and h > 12:
        new_contours.append(cnt)

for cnt in new_contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x-5, y-5), (x + w+5, y + h+5), (0, 0, 255), 2)
cv2.imshow('final', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('bounded.jpeg', img)
cv2.imwrite('dilated.jpeg', dilation)

# import numpy as np
# import matplotlib.pyplot as plt
#
# import pathlib
# import cv2
# import os
# import sys
#
# # import PIL.Image as Image
#
# notes = cv2.imread("part1.jpeg", cv2.IMREAD_GRAYSCALE)
# #notes = cv2.resize(notes, )
# notes = cv2.cvtColor(notes, cv2.COLOR_BGR2RGB)
#
# _, bin_notes = cv2.threshold(notes, 120, 255, cv2.THRESH_BINARY)
#
# black = np.zeros(bin_notes.shape)
# black_1 = np.zeros(bin_notes.shape)
#
#
# kernel_f = np.array([[-2, -2, -2], [1, 1, 1], [2, 2, 2]], np.float32)
# img_filter = cv2.filter2D(notes, -1, kernel_f)
#
# BinGray = cv2.Canny(img_filter, 900, 100, 10)
#
# contours, hierarchy = cv2.findContours(BinGray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#
#
# new_contours = contours[:300]
#
#
#
# cv2.drawContours(black, contours, -1, (0, 255, 0), 1)
# cv2.imshow('contours', black)
#
# cv2.drawContours(black_1, new_contours, -1, (0, 255, 0), 1)
# cv2.imshow('new_contours', black_1)
#
# print("contours",len(contours))
# print("new_contours",len(new_contours))
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
