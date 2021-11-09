import cv2
import numpy as np


img = cv2.imread("Resources/card.jpg")

whidth, hight = 250, 350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [whidth, 0], [0, hight], [whidth, hight]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imhOutput = cv2.warpPerspective(img, matrix, (whidth, hight))


cv2.imshow("Image", img)
cv2.imshow("Output", imhOutput)
cv2.waitKey(0)
