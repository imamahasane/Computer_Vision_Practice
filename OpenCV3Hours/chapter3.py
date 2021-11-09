import cv2


img = cv2.imread("Resources/lamdo.png")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)


cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.waitKey(0)
