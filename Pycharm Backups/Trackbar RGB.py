import cv2
import numpy as np

def value(x):
    rValue = cv2.getTrackbarPos('R', 'Yaar Tera')
    gValue = cv2.getTrackbarPos('G', 'Yaar Tera')
    bValue = cv2.getTrackbarPos('B', 'Yaar Tera')

    img[:] = [bValue, gValue, rValue]

    print('R: '+str(rValue)+"  G: "+str(gValue)+"  B: "+str(bValue))

# def valueG(x):
#     print("G: "+str(x))
# def valueB(x):
#     print("B: "+str(x))

img = np.zeros((300,512,3) , np.uint8)
cv2.namedWindow('Yaar Tera')

cv2.createTrackbar('R', 'Yaar Tera', 0,255, value)
cv2.createTrackbar('G', 'Yaar Tera', 0,255, value)
cv2.createTrackbar('B', 'Yaar Tera', 0,255, value)






while(1):
    cv2.imshow('Yaar Tera', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cv2.destroyAllWindows()