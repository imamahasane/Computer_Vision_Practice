import cv2

faceCascde = cv2.CascadeClassifier("/Users/macbookair/Python/OpenCV/data/haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)

while True:
    nongare, image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = faceCascde.detectMultiScale(image, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Image Fream", image)
        k = cv2.waitKey(30) & 0xFF

        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()