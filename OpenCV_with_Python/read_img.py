import cv2 as cv

img = cv.imread('/Users/imamahasan/python/OpenCV_with_Python/Photos/cat_large.jpg')
cv.imshow("Cat", img)

cv.waitKey(0)
