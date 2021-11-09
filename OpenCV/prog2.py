
import cv2

path = r'/Users/macbookair/Python/OpenCV/image/imam.jpeg'
image = cv2.imread(path, 0)
window_name = 'image'

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
