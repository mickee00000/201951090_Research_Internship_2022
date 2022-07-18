import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Sudoku.jpg")
img = cv.resize(img, (500,500))
_,img = cv.threshold(img, 150,255, cv.THRESH_BINARY)

edges = cv.Canny(img, 50,150, apertureSize = 3)
Lines = cv.HoughLines(edges, 1, np.pi/180, 200)

print(Lines)

for line in Lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a + rho
    y0 = b + rho

    x1 = int(x0 + 1000*(-b))
    x2 = int(x0 - 1000*(-b))

    y1 = int(y0 + 1000*(a))
    y2 = int(y0 - 1000*(a))


    cv.line(img, (x1,y1), (x2,y2), (255,255,255), 5)


cv.imshow('sudoko', img)
cv.waitKey(0)
cv.destroyAllWindows()