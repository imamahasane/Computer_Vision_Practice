import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

#imgHor = np.hstack((img, img))
#imgVer = np.vstack((img, img))

#cv2.imshow("Horizontal", imgHor)
#cv2.imshow("Vertical", imgVer)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))
cv2.imshow("Stack Image", imgStack)

cv2.waitKey(0)
