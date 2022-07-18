#import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

import pathlib
import cv2
import os
import sys
#import PIL.Image as Image

notes = cv2.imread("part1.jpeg", cv2.IMREAD_GRAYSCALE)
notes = cv2.cvtColor(notes, cv2.COLOR_BGR2RGB)

_ , bin_notes = cv2.threshold(notes, 120, 255, cv2.THRESH_BINARY)

black = np.zeros(bin_notes.shape)

BinGray = cv2.Canny(bin_notes, 900, 100, 10)

contours, hierarchy = cv2.findContours(BinGray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(notes, contours,-1, (0,255,0), 1)
cv2.imshow('bin_notes', notes)

print(len(contours))

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(notes, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imshow('final', notes)

cv2.imwrite('contour_drawn.jpeg', notes )


cv2.waitKey(0)