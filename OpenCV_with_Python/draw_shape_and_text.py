import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank Image", blank)

# 1. paint image
blank[:] = 0, 255, 0
cv.imshow('Green Image', blank)

blank[:] = 0, 0, 255
cv.imshow('Read Image', blank)

blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green Image 2', blank)

# 2. Drow a Rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness= 2)
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness= -1)
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness= cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Drow a Circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)
cv.imshow("Circle", blank)

cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank)

# 4 Drow Line
cv.line(blank, (100, 250), (blank.shape[1] // 2, blank.shape[0] // 2),   (255, 255, 255), thickness= 3)
cv.imshow("Line", blank) 

cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness= 3)
cv.imshow("Line", blank) 

# 5 Write text
cv.putText(blank, "Hello, my name is Imam!!!", (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

 
cv.waitKey(0)