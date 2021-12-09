import cv2 as cv

img = cv.imread('/Users/imamahasan/python/OpenCV_with_Python/Photos/park.jpg')
cv.imshow("Park", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Park", gray)

# Blur 
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur Park", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edge Park", canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Blur Edge Park", canny)

# Dilating Image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated Park", dilated)

# Eroding 
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Eroded Park", eroded)

# Resize
resize = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow("Resize img", resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)