import numpy as np
import cv2 as cv

img = cv.imread('images.png')
img = cv.resize(img, (520,320))

img_gr = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_ , img_th = cv.threshold(img_gr, 240, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(img_th, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour , True), True)
    cv.drawContours(img, [approx], 0, (0,255,0), 5)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv.putText(img, "Triangle", (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
    elif  len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 4:
        x,y,w,h = cv.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.75 < aspect_ratio < 1.25:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))


print(approx, len(approx))

print(len(contours) - 1)



cv.drawContours(img, contours,5, (0,255,0), 3)


cv.imshow('image', img)
cv.waitKey(0)