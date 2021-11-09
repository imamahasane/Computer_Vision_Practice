import cv2

image = cv2.imread("/Users/macbookair/Python/OpenCV/image/imam.jpeg")
ImgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ImgBlur = cv2.GaussianBlur(ImgGray, (99, 99), 0)
cv2.imshow("Orginal Image", image)
cv2.imshow("Gray Image", ImgGray)
cv2.imshow("Blur Image", ImgBlur)

cv2.waitKey(0)